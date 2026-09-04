<?php
// Deploy OUTSIDE the public document root as gentech-form-private/config.php.
// Never put real credentials in Git, browser JavaScript, or an upload over plain FTP.
return [
    'enabled' => false,
    'origin' => 'https://serhatramay.github.io',
    'smtp_host' => 'smtp.markum.net',
    'smtp_port' => 587,
    'smtp_user' => 'info@gentech.ae',
    'smtp_password' => '',
    'signing_key' => '', // At least 32 random bytes, encoded as a string.
    'state_directory' => __DIR__ . '/var',
];
