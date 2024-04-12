# My puppet manifest to fix apache

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin']
}
