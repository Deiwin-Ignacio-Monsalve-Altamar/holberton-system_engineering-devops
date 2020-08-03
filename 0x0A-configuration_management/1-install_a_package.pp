#Using Puppet, install puppet-lint

package { 'puppet-lint':
ensure     => installed,
source     => 'gem install puppet-lint -v 2.1.1'
}
