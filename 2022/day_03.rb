#!/usr/bin/env ruby

path = ARGV[0] || File.join(__dir__, "inputs", "example_03.txt")

rucksacks = File.read(path).split("\n")

def reduce_to_item_priority(items)
  (items.reduce(&:intersection).first.ord + 20) % 58
end

def part_1(data)
  data
    .map { _1.each_char.each_slice(_1.size / 2) }
    .map { reduce_to_item_priority _1 }
    .sum
end

def part_2(data)
  data
    .map(&:chars)
    .each_slice(3)
    .map { reduce_to_item_priority _1 }
    .sum
end

puts part_1(rucksacks)
puts part_2(rucksacks)
