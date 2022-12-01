#!/usr/bin/env ruby

file = !ARGV.empty? ? ARGV[0] : "inputs/example_01.txt"

data = File.read(file)
  .split("\n\n")
  .map { _1.split.map(&:to_i) }

def part_1(data)
  data.map(&:sum).max
end

def part_2(data)
  data.map(&:sum).sort.reverse.take(3).sum
end

puts part_1(data)
puts part_2(data)
