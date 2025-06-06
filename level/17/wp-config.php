<?php
define( 'DB_NAME', 'wordpress_db' );
define( 'DB_USER', 'wordpress-user' );
define( 'DB_PASSWORD', '\$uper\$ecureP@55w0rd!123' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8' );
define( 'DB_COLLATE', '' );
// ... (rest of salts & keys)
$table_prefix = 'wp_';
define( 'WP_DEBUG', false );
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}
require_once ABSPATH . 'wp-settings.php';
