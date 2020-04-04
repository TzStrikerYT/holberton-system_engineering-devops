#install nginx
exec {'/usr/bin/env apt-get -y update': }
exec {'/usr/bin/env apt-get -y install nginx': }

-> file_line { "Add_header" :
   ensure => present,
   path   => "/etc/nginx/sites-available/default",
   line   => "\tadd_header X-Served-By ${hostname};",
   after  => "server_name_;",
}

exec { '/usr/bin/env service nginx start': }