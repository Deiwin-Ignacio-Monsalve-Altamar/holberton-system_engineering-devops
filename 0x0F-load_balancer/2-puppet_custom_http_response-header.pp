# install nginx
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt',
}


file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By \$hostname;",
  after   => '^server {$',
  require => Package['nginx'],
}

# start server.

service { 'nginx':
  ensure => running,
  enable => true,
}
