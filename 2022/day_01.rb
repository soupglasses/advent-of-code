#!/usr/bin/env ruby

file = !ARGV.empty? ? ARGV[0] : "inputs/example_01.txt"

sums_of_calories = File.read(file)
  .split("\n\n")
  .map { _1.split.map(&:to_i).sum }

def part_1(data)
  data.max
end

def part_2(data)
  data.sort.reverse.take(3).sum
end

puts part_1(sums_of_calories)
puts part_2(sums_of_calories)
