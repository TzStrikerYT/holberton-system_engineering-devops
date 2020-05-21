#chage name of the file to fix error 500
exec { '/bin/bash':
  command => 'sudo mv /var/www/html/wp-includes/class-wp-locale.php /var/www/ht\
ml/wp-includes/class-wp-locale.phpp',
  creates => "sudo mv /var/www/html/wp-includes/class-wp-locale.phpp",
  path    => ["/usr/bin", "/usr/sbin"],
}

service { 'apache2':
  ensure  => running,
  restart => 'sudo service apache2 start',
}