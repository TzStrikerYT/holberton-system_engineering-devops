#puppet change value
exec {'/usr/bin/env': 
  command => 'sed -i "s/15/1000/" /etc/default/nginx ; sudo service nginx restart',
  path    =>  ['/usr/bin', '/bin'],
}
