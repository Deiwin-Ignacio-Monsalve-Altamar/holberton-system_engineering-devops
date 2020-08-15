#Nginx server so that /redirect_me is redirecting to another page
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    require => Package['nginx'],
  }

  file_line { 'custom_header':
    path    => '/etc/nginx/sites-available/default',
    line    => "\tadd_header X-Served-By \$hostname;",
    match   => '^server {$',
    match_for_absence => true,
}
