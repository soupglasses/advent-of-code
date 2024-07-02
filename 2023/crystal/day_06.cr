#!/usr/bin/env crystal

require "big"

def next_digit(float : BigFloat) : BigInt
  float.ceil.to_big_i
end

def prev_digit(float : BigFloat) : BigInt
  -next_digit(-float)
end

def parse(data : String) : Array(Tuple(BigInt, BigInt))
  time, distance = data.split("\n")

  times = time[5..].split.map(&.to_big_i)
  distances = distance[9..].split.map(&.to_big_i)

  times.zip(distances)
end

def total_faster_solutions(time_ms : BigInt, record_distance : BigInt) : BigInt
  # Find roots of: x^2 - tx + d < 0
  a, b, c = 1, -time_ms, record_distance

  d = Math.sqrt(b**2 - 4*a*c)
  x_max = (-b + d) / 2*a
  x_min = (-b - d) / 2*a

  # Return inclusive size of integer solutions
  prev_digit(x_max) - next_digit(x_min) + 1
end

def part1(races : Array(Tuple(BigInt, BigInt))) : BigInt
  # TODO: Figure out why example gives the wrong answer for part1, but input works correctly.
  races.map { |race| total_faster_solutions(race[0], race[1]) }.product
end

def part2(races : Array(Tuple(BigInt, BigInt))) : BigInt
  race = races.transpose.map { |race| race.map(&.to_s).join("").to_big_i }
  total_faster_solutions(race[0], race[1])
end

data = parse(File.read("../inputs/example_06.txt"))
puts(part1(data))
puts(part2(data))
