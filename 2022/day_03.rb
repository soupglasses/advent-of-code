#!/usr/bin/env ruby

require 'set'

path = ARGV[0] || File.join(__dir__, "inputs", "example_03.txt")

rucksacks = File.read(path)
  .split("\n")

def letter_priority(char)
  char.ord - (char.match?(/[a-z]/) ? "a".ord - 1 : "A".ord - 27)
end

def part_1(data)
  data
    .map { _1.each_char.each_slice(_1.size / 2).map(&:join) }
    .map { (_1[0].chars & _1[1].chars).first }
    .map { letter_priority(_1) }
    .sum
end

def part_2(data)
  data
    .map { _1.each_char.to_set }
    .each_slice(3)
    .map { _1.reduce(&:intersection) }
    .map(&:first)
    .map { letter_priority(_1) }
    .sum
end

puts part_1(rucksacks)
puts part_2(rucksacks)
