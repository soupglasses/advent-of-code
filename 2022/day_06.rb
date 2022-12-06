#!/usr/bin/env ruby

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_06.txt")

datastream = File.read(PATH).chomp

def start_of_packet_by_size(data, size)
  data
    .chars
    .each_cons(size)
    .with_index
    .filter { |a, _| a.uniq.length == a.length }
    .first
    .then { |_, i| i + size }
end

def part_1(data)
  start_of_packet_by_size(data, 4)
end

def part_2(data)
  start_of_packet_by_size(data, 14)
end

puts part_1(datastream)
puts part_2(datastream)
