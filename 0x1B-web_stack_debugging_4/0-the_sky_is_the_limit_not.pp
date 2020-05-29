# puppet change value
exec { '/bin/bash':
  command => 'sed -i "s/15/1000/" /etc/default/nginx ; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
