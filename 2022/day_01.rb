#!/usr/bin/env ruby

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_01.txt")

sums_of_calories = File.read(PATH)
  .split("\n\n")
  .map { _1.split("\n").map(&:to_i).sum }

def part_1(data)
  data.max
end

def part_2(data)
  data.max(3).sum
end

puts part_1(sums_of_calories)
puts part_2(sums_of_calories)
