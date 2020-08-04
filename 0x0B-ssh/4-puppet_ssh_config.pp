#!/usr/bin/env bash
#Let’s practice using Puppet to make changes
file_line { 'IdentityFile'
  ensure => present,
  path   => '/tmp/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile'
}
file_line { 'PasswordAuthentication'
  ensure => present,
  path   => '/tmp/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication'
}
