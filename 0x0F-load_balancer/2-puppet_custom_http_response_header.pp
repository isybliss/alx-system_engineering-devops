# Automate the creation of HTTP header response using puppet

exec {'update':
  command => 'sudo apt-get update',
  provider => shell,
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line {'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

-> exec {'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
