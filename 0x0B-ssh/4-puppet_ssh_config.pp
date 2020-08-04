#!/usr/bin/env bash
#Let’s practice using Puppet to make changes
file { 'config'
path    => '~/.ssh/',
mode    =>  '0600',
content => 'Host ubuntu@35.196.97.61
    HostName ubuntu@35.196.97.61
    User ubuntu
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no'
}
