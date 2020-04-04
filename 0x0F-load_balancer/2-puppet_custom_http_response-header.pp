#install nginx
exec {'/usr/bin/env apt-get -y update': }
exec {'/usr/bin/env apt-get -y install nginx': }
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }

-> file_line { "Add_header" :
   ensure => present,
   path   => '/etc/nginx/sites-available/default',
   line   => "\tadd_header X-Served-By ${hostname};",
   after  => 'server_name _;',
}

exec { '/usr/bin/env service nginx start': }