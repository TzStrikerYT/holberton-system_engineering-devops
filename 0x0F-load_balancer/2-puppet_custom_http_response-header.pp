#install nginx
exec {'/usr/bin/env sudo apt-get -y update': }
exec {'/usr/bin/env sudo apt-get -y install nginx': }
exec {'/usr/bin/env sudo echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env sudo sed -i "26i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf': }
exec {'/usr/bin/env sudo service nginx start': }