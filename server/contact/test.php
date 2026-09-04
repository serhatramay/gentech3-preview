<?php
declare(strict_types=1);
require __DIR__ . '/app.php';
$directory = sys_get_temp_dir() . '/gentech-contact-test-' . bin2hex(random_bytes(8));
$config = ['enabled' => true, 'origin' => 'https://serhatramay.github.io', 'smtp_user' => 'info@gentech.ae', 'smtp_password' => 'TEST-ONLY', 'signing_key' => str_repeat('test-only-', 4), 'state_directory' => $directory];
$app = new GentechContact($config);
$now = 1788552000;
$sent = [];
$send = static function ($fields, $id) use (&$sent): void { $sent[] = [$fields, $id]; };
$count = 0;
function check(bool $condition, string $label): void { global $count; if (!$condition) throw new RuntimeException('FAIL: ' . $label); $count++; echo "PASS: $label\n"; }
function request(string $method, string $body = '', string $ip = '192.0.2.1', ?int $time = null, ?callable $callback = null): array {
    global $app, $config, $now, $send;
    return $app->handle($method, $config['origin'], 'application/json', $body, $ip, $time ?? $now, $callback ?? $send);
}
function fields(string $ip = '192.0.2.1', ?int $time = null): array {
    return ['name' => 'Test User', 'email' => 'visitor@example.com', 'company' => 'Test company', 'department' => 'cards', 'message' => 'This is a local test; no real email is sent.', 'consent' => true, 'website' => '', 'token' => request('GET', '', $ip, $time)[1]['token']];
}
try {
    check(request('OPTIONS')[0] === 204, 'CORS preflight');
    check($app->handle('GET', 'https://other.example', '', '', '192.0.2.1', $now, $send)[0] === 403, 'reject foreign origin');
    check($app->handle('GET', '', '', '', '192.0.2.1', $now, $send)[0] === 403, 'reject absent origin');
    check(request('PUT')[0] === 405, 'reject unsupported methods');
    check(request('POST', str_repeat('x', 16385))[0] === 413, 'request size cap');
    check(request('POST', '{broken')[0] === 400, 'malformed JSON');
    check(request('POST', '[]')[0] === 422, 'reject list payload');
    check($app->handle('POST', $config['origin'], 'text/plain', '{}', '192.0.2.1', $now, $send)[0] === 415, 'reject non-JSON');
    $f = fields();
    check(request('POST', json_encode($f))[0] === 422, 'minimum fill interval');
    check(request('POST', json_encode($f), '192.0.2.2', $now + 4)[0] === 422, 'token bound to address');
    check(request('POST', json_encode($f), '192.0.2.1', $now + 1801)[0] === 422, 'expired token');
    foreach (['name' => "X\r\nBcc: attack@example.com", 'email' => 'bad@@example.com', 'company' => str_repeat('x', 161), 'department' => 'attacker@example.com', 'message' => 'short', 'consent' => false, 'website' => 'spam', 'token' => str_repeat('x', 110)] as $field => $value) {
        $bad = $f; $bad[$field] = $value;
        check(request('POST', json_encode($bad), '192.0.2.1', $now + 4)[0] === 422, 'reject invalid ' . $field);
    }
    $bad = $f; $bad['to'] = 'attacker@example.com';
    check(request('POST', json_encode($bad), '192.0.2.1', $now + 4)[0] === 422, 'cannot inject recipient');
    check(count($sent) === 0, 'invalid inputs never invoke transport');
    $ok = request('POST', json_encode($f), '192.0.2.1', $now + 4);
    check($ok[0] === 200 && $ok[1]['ok'] === true && count($sent) === 1, 'accepted transport returns reference');
    check(request('POST', json_encode($f), '192.0.2.1', $now + 5) === $ok && count($sent) === 1, 'idempotent replay without duplicate');
    $changed = $f; $changed['message'] .= ' Changed';
    check(request('POST', json_encode($changed), '192.0.2.1', $now + 5)[0] === 409, 'cannot reuse token for changed content');
    $failed = fields('192.0.2.2');
    $error = request('POST', json_encode($failed), '192.0.2.2', $now + 4, static function (): void { throw new RuntimeException('SECRET SMTP ERROR'); });
    check($error[0] === 503 && $error[1]['error'] === 'unconfirmed', 'SMTP failure never reports success');
    check(request('POST', json_encode($failed), '192.0.2.2', $now + 5)[0] === 409 && count($sent) === 1, 'uncertain send is not automatically repeated');
    for ($i = 0; $i < 2; $i++) { $more = fields(); check(request('POST', json_encode($more), '192.0.2.1', $now + 4)[0] === 200, 'within per-IP budget'); }
    check(request('POST', json_encode(fields()), '192.0.2.1', $now + 4)[0] === 429, 'rate limit');
    $state = file_get_contents($directory . '/requests.json');
    check(!str_contains($state, 'visitor@example.com') && !str_contains($state, 'Test User') && !str_contains($state, '192.0.2.'), 'state does not store raw visitor identity or message');
    $locked = fopen($directory . '/requests.lock', 'c'); flock($locked, LOCK_EX);
    check(request('POST', json_encode(fields('192.0.2.3')), '192.0.2.3', $now + 4)[1]['error'] === 'busy', 'concurrent sends fail safely without waiting');
    flock($locked, LOCK_UN); fclose($locked);
    $disabled = new GentechContact(array_replace($config, ['enabled' => false]));
    check($disabled->handle('GET', $config['origin'], '', '', '192.0.2.1', $now, $send)[0] === 503, 'disabled until provisioned');
    $text = GentechContact::emailBody($f, $ok[1]['reference']);
    check(str_contains($text, 'Cards & samples') && str_contains($text, $f['message']), 'topic and message retained in email');
    echo "$count checks passed. Transport was a local stub; no email sent.\n";
} finally {
    foreach (['requests.json', 'requests.json.new', 'requests.lock'] as $name) { if (is_file($directory . '/' . $name)) unlink($directory . '/' . $name); }
    if (is_dir($directory)) rmdir($directory);
}
