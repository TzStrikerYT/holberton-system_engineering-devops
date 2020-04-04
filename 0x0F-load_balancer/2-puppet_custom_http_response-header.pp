#install nginx
exec { 'Update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'Installer':
  require  => Exec['Update'],
  command  => '/usr/bin/env sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'add_http':
  require  => Exec['Installer'],
  command  => '/usr/bin/env sudo sed -i "35i\     add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'start_nginx':
  require  => Exec['add_http'],
  command  => '/usr/bin/env sudo service nginx start',
  provider => shell,
}