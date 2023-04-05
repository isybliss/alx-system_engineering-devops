# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec { 'server configuration':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" | sudo tee /var/www/html/index.html; sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4\/;\\n\\t}/" /etc/nginx/sites-available/default; sudo service nginx restart'
}
