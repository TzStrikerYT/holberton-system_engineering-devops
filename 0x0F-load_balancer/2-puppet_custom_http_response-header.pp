#install nginx
exec { 'Update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'Instaler':
  command  => '/usr/bin/env sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'add_http':
  command  => '/usr/bin/env sudo sed -i "26i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf',
  provider => shell,
}

exec { 'start_nginx':
  command  => '/usr/bin/env sudo service nginx start',
  provider => shell,
}