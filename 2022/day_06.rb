#!/usr/bin/env ruby

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_06.txt")

datastream = File.read(PATH).chomp

def packet_offset_from_size(data, size)
  data
    .each_char
    .each_cons(size)
    .find_index { _1.uniq.length == size }
    &.then { _1 + size }
end

def part_1(data)
  packet_offset_from_size(data, 4)
end

def part_2(data)
  packet_offset_from_size(data, 14)
end

puts part_1(datastream)
puts part_2(datastream)
