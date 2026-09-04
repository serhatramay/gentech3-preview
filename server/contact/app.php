<?php
declare(strict_types=1);

final class GentechContact
{
    public const TOPICS = [
        'general' => 'General enquiry', 'capital' => 'Capital & strategic investments',
        'infrastructure' => 'Infrastructure development', 'mobility' => 'National mobility program',
        'payments' => 'Payment technologies', 'telecom' => 'Connected devices',
        'cards' => 'Cards & samples', 'partnerships' => 'Partnerships',
        'canada' => 'Toronto office', 'uae' => 'Ras Al Khaimah office', 'africa' => 'Johannesburg office',
    ];

    public function __construct(private array $config) {}

    private function failure(int $status, string $code): array
    {
        return [$status, ['ok' => false, 'error' => $code]];
    }

    public function handle(string $method, string $origin, string $type, string $body, string $ip, int $now, callable $send): array
    {
        if ($origin !== $this->config['origin'] || $origin === '') return $this->failure(403, 'origin');
        if ($method === 'OPTIONS') return [204, []];
        if (!in_array($method, ['GET', 'POST'], true)) return $this->failure(405, 'method');
        if (empty($this->config['enabled']) || strlen($this->config['signing_key'] ?? '') < 32
            || empty($this->config['smtp_password'])
            || !preg_match('/\A[A-Za-z0-9._+\-]+@gentech\.ae\z/', $this->config['smtp_user'] ?? '')) {
            return $this->failure(503, 'unavailable');
        }
        $key = $this->config['signing_key'];
        $ipHash = hash_hmac('sha256', $ip, $key);
        if ($method === 'GET') {
            $claim = $now . '.' . bin2hex(random_bytes(16));
            return [200, ['ok' => true, 'token' => $claim . '.' . hash_hmac('sha256', $claim . '.' . $ipHash, $key), 'minimumWaitMs' => 3000]];
        }
        if (strlen($body) > 16384) return $this->failure(413, 'too_large');
        if (strtolower(trim(explode(';', $type)[0])) !== 'application/json') return $this->failure(415, 'content_type');
        try { $data = json_decode($body, true, 8, JSON_THROW_ON_ERROR); }
        catch (Throwable $error) { return $this->failure(400, 'invalid'); }
        if (!is_array($data) || array_is_list($data)) return $this->failure(422, 'invalid');
        $expected = ['name', 'email', 'company', 'department', 'message', 'consent', 'website', 'token'];
        if (array_diff(array_keys($data), $expected) || array_diff($expected, array_keys($data))) return $this->failure(422, 'invalid');
        if ($data['consent'] !== true || $data['website'] !== '') return $this->failure(422, 'invalid');
        foreach (['name' => [1, 100], 'email' => [3, 180], 'company' => [0, 160], 'department' => [1, 30], 'message' => [10, 2500]] as $field => $limits) {
            if (!is_string($data[$field]) || !preg_match('//u', $data[$field])) return $this->failure(422, 'invalid');
            $data[$field] = trim($data[$field]);
            $length = preg_match_all('/./us', $data[$field]);
            if ($length < $limits[0] || $length > $limits[1]) return $this->failure(422, 'invalid');
            $controls = $field === 'message' ? '/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/' : '/[\x00-\x1f\x7f]/';
            if (preg_match($controls, $data[$field])) return $this->failure(422, 'invalid');
        }
        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL) || !isset(self::TOPICS[$data['department']])) return $this->failure(422, 'invalid');
        if (!is_string($data['token']) || !preg_match('/\A(\d{10})\.([a-f0-9]{32})\.([a-f0-9]{64})\z/', $data['token'], $token)) return $this->failure(422, 'token');
        $age = $now - (int)$token[1];
        if ($age < 3 || $age > 1800 || !hash_equals(hash_hmac('sha256', $token[1] . '.' . $token[2] . '.' . $ipHash, $key), $token[3])) return $this->failure(422, 'token');

        $directory = $this->config['state_directory'];
        if (!is_dir($directory) && !mkdir($directory, 0700, true) && !is_dir($directory)) return $this->failure(503, 'unavailable');
        $lock = fopen($directory . '/requests.lock', 'c');
        if ($lock === false) return $this->failure(503, 'unavailable');
        if (!flock($lock, LOCK_EX | LOCK_NB)) { fclose($lock); return $this->failure(503, 'busy'); }
        try {
            $file = $directory . '/requests.json';
            $state = is_file($file) ? json_decode(file_get_contents($file), true, 8, JSON_THROW_ON_ERROR) : [];
            if (!is_array($state)) throw new RuntimeException('Invalid state');
            $state = array_filter($state, static fn(array $r): bool => $r['time'] > $now - 86400);
            $fingerprint = hash_hmac('sha256', json_encode(array_intersect_key($data, array_flip(['name', 'email', 'company', 'department', 'message', 'consent']))), $key);
            $id = 'GT-' . strtoupper($token[2]);
            if (isset($state[$id])) {
                if (!hash_equals($state[$id]['fingerprint'], $fingerprint)) return $this->failure(409, 'changed');
                return $state[$id]['status'] === 'accepted'
                    ? [200, ['ok' => true, 'reference' => $id]] : $this->failure(409, 'unconfirmed');
            }
            $hour = 0; $ipQuarter = 0; $ipDay = 0;
            foreach ($state as $row) {
                if ($row['time'] > $now - 3600) $hour++;
                if (hash_equals($row['ip'], $ipHash)) {
                    $ipDay++;
                    if ($row['time'] > $now - 900) $ipQuarter++;
                }
            }
            // Intentionally conservative limits for the public test endpoint.
            if (count($state) >= 50 || $hour >= 20 || $ipDay >= 6 || $ipQuarter >= 3) return $this->failure(429, 'rate_limit');
            // Persist BEFORE contacting SMTP. A timeout/crash must not cause an automatic duplicate.
            $state[$id] = ['time' => $now, 'ip' => $ipHash, 'fingerprint' => $fingerprint, 'status' => 'unconfirmed'];
            $this->persist($file, $state);
            try { $send($data, $id); }
            catch (Throwable $error) { return $this->failure(503, 'unconfirmed'); }
            $state[$id]['status'] = 'accepted';
            $this->persist($file, $state);
            return [200, ['ok' => true, 'reference' => $id]];
        } catch (Throwable $error) {
            return $this->failure(503, 'unavailable');
        } finally {
            flock($lock, LOCK_UN);
            fclose($lock);
        }
    }

    private function persist(string $file, array $state): void
    {
        $temp = $file . '.new';
        $json = json_encode($state, JSON_THROW_ON_ERROR);
        if (file_put_contents($temp, $json, LOCK_EX) !== strlen($json)) throw new RuntimeException('State unavailable');
        chmod($temp, 0600);
        if (!rename($temp, $file)) throw new RuntimeException('State unavailable');
    }

    public static function emailBody(array $fields, string $id): string
    {
        return "GENTECH WEBSITE PREVIEW ENQUIRY\n\nReference: {$id}\nName: {$fields['name']}\nEmail: {$fields['email']}\nCompany: "
            . ($fields['company'] ?: 'Not provided') . "\nTopic: " . self::TOPICS[$fields['department']]
            . "\n\n{$fields['message']}\n\nThe sender agreed to use these details to respond to this enquiry.\n"
            . "Submitted through the GitHub website preview; topic labels do not imply automatic departmental forwarding.\n";
    }
}
