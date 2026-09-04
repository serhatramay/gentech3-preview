<?php
declare(strict_types=1);
// Only this entry point belongs in the test subdomain's document root.
ini_set('display_errors', '0');
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');
header('X-Robots-Tag: noindex, nofollow');
header('Referrer-Policy: no-referrer');
header("Content-Security-Policy: default-src 'none'; frame-ancestors 'none'");
try {
    $private = dirname(__DIR__) . '/gentech-form-private';
    if (!is_file($private . '/config.php') || !is_file($private . '/app.php')) {
        throw new RuntimeException('Not provisioned');
    }
    require $private . '/app.php';
    $config = require $private . '/config.php';
    // Do not trust arbitrary X-Forwarded-Proto or X-Forwarded-For headers.
    if (($_SERVER['HTTPS'] ?? '') !== 'on') {
        http_response_code(403);
        echo json_encode(['ok' => false, 'error' => 'https_required']);
        exit;
    }
    $app = new GentechContact($config);
    $origin = $_SERVER['HTTP_ORIGIN'] ?? '';
    if ($origin === $config['origin']) {
        header('Access-Control-Allow-Origin: ' . $origin);
        header('Vary: Origin');
        header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
        header('Access-Control-Allow-Headers: Content-Type');
    }
    $result = $app->handle(
        $_SERVER['REQUEST_METHOD'], $origin,
        $_SERVER['CONTENT_TYPE'] ?? '',
        (string)file_get_contents('php://input', false, null, 0, 16385),
        $_SERVER['REMOTE_ADDR'] ?? '', time(),
        static function (array $fields, string $id) use ($config, $private): void {
            require_once $private . '/vendor/autoload.php';
            $mail = new PHPMailer\PHPMailer\PHPMailer(true);
            $mail->isSMTP();
            $mail->Host = $config['smtp_host'];
            $mail->Port = $config['smtp_port'];
            $mail->SMTPAuth = true;
            $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Username = $config['smtp_user'];
            $mail->Password = $config['smtp_password'];
            $mail->SMTPDebug = 0;
            $mail->Timeout = 10;
            $mail->Timelimit = 15;
            $mail->CharSet = 'UTF-8';
            $mail->Encoding = 'base64';
            $mail->setFrom($config['smtp_user'], 'Gentech website preview');
            // Neither recipient nor sender can be supplied by the visitor.
            $mail->addAddress('info@gentech.ae', 'Gentech enquiries');
            $mail->addReplyTo($fields['email'], $fields['name']);
            $mail->Subject = '[Website preview] Gentech enquiry - ' . GentechContact::TOPICS[$fields['department']];
            $mail->MessageID = '<' . $id . '@forms-preview.gentech.ae>';
            $mail->isHTML(false);
            $mail->Body = GentechContact::emailBody($fields, $id);
            $mail->send();
        }
    );
    http_response_code($result[0]);
    if ($result[0] === 429) header('Retry-After: 900');
    if ($result[0] !== 204) echo json_encode($result[1]);
} catch (Throwable $error) {
    // Do not expose SMTP details, credentials, paths or visitor data.
    http_response_code(503);
    echo json_encode(['ok' => false, 'error' => 'unavailable']);
}
