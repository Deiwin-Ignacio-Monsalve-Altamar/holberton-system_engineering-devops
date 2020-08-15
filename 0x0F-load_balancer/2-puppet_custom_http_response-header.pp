exec { 'update':
  command => 'sudo apt-get update -y'
  path    => ['/usr/bin', '/bin']
}

# install nginx
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt',
  require => Exec['update'],
}


file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By ${hostname};",
  after   => 'listen 80 default_server;',
  require => Package['nginx'],
}

# start server.

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => file_line['custom_header'],
}
