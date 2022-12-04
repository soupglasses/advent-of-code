#!/usr/bin/env ruby

require "set"

path = ARGV[0] || File.join(__dir__, "inputs", "example_04.txt")

camp_sections = File.read(path)
  .split("\n")
  .map { |line|
  line
    .split(/,|-/)
    .map(&:to_i)
    .each_slice(2)
    .map { Range.new(_1, _2).to_set }
}

def part_1(data)
  data
    .map { _1.subset?(_2) || _1.superset?(_2) }
    .count(true)
end

def part_2(data)
  data
    .map { _1.intersect? _2 }
    .count(true)
end

puts part_1(camp_sections)
puts part_2(camp_sections)
