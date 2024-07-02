#!/usr/bin/env crystal

def next_digit(float : Float64) : Int64
  float % 1 == 0.0 ? float.to_i64 + 1 : float.ceil.to_i64
end

def prev_digit(float : Float64) : Int64
  -next_digit(-float)
end

def parse(data : String) : Array(Tuple(Int64, Int64))
  time, distance = data.split("\n")

  times = time[5..].split.map(&.to_i64)
  distances = distance[9..].split.map(&.to_i64)

  times.zip(distances)
end

def total_faster_solutions(time_ms : Int64, record_distance : Int64) : Int64
  # Find roots of: x^2 - tx + d < 0
  a, b, c = 1, -time_ms, record_distance

  d = Math.sqrt(b**2 - 4*a*c)
  x_max = (-b + d) / 2*a
  x_min = (-b - d) / 2*a

  # Return inclusive size of integer solutions
  prev_digit(x_max) - next_digit(x_min) + 1
end

def part1(races : Array(Tuple(Int64, Int64))) : Int64
  races.map { |race| total_faster_solutions(race[0], race[1]) }.product
end

def part2(races : Array(Tuple(Int64, Int64))) : Int64
  race = races.transpose.map { |race| race.map(&.to_s).join("").to_i64 }
  total_faster_solutions(race[0], race[1])
end

data = parse(File.read("../inputs/example_06.txt"))
puts(part1(data))
puts(part2(data))
