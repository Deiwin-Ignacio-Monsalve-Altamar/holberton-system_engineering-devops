#!/usr/bin/env ruby
variable_from = ARGV[0].scan(/from:(.\w+)/).join
variable_to = ARGV[0].scan(/to:(.\d+)/).join
variable_flags = ARGV[0].scan(/flags:(.+-\d)/).join
puts "#{variable_from},#{variable_to},#{variable_flags}"
