#!/usr/bin/env ruby

path = ARGV[0] || File.join(__dir__, "inputs", "example_04.txt")

camp_sections = File.foreach(path, chomp: true)
  .map { |line|
  line
    .split(/,|-/)
    .map(&:to_i)
    .each_slice(2)
    .map { _1.._2 }
}

def disjoint?(r1, r2)
  (r1.begin <= r2.begin && r2.begin <= r1.end) || (r2.begin <= r1.begin && r1.begin <= r2.end)
end

def part_1(data)
  data
    .filter { _1.cover?(_2) || _2.cover?(_1) }
    .count
end

def part_2(data)
  data
    .filter { disjoint?(_1, _2) }
    .count
end

puts part_1(camp_sections)
puts part_2(camp_sections)
