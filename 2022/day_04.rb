#!/usr/bin/env ruby

require 'set'

path = ARGV[0] || File.join(__dir__, "inputs", "example_04.txt")

camp_sections = File.foreach(path, chomp: true)
  .map { |line|
  line
    .split(/,|-/)
    .map(&:to_i)
    .each_slice(2)
    .map { Range.new(_1, _2).to_set }
}

def part_1(data)
  data
    .filter { _1.subset?(_2) || _2.subset?(_1) }
    .count
end

def part_2(data)
  data
    .filter { _1.intersect?(_2) }
    .count
end

puts part_1(camp_sections)
puts part_2(camp_sections)
