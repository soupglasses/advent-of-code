#!/usr/bin/env ruby

def next_digit(float)
  float % 1 == 0.0 ? float.to_i + 1 : float.ceil
end

def prev_digit(float)
  -next_digit(-float)
end

def parse(file)
  time, distance = File.readlines(file, trim: true)

  times = time[5..].split.map(&:to_i)
  distances = distance[9..].split.map(&:to_i)

  times.zip(distances)
end

def total_faster_solutions(time_ms, record_distance)
  # Find roots of: x^2 - tx + d < 0
  a, b, c = 1, -time_ms, record_distance

  d = Math.sqrt(b**2 - 4*a*c)
  x_max = (-b + d) / 2*a
  x_min = (-b - d) / 2*a

  # Return inclusive size of integer solutions
  prev_digit(x_max) - next_digit(x_min) + 1
end

def part1(races)
  races.map { total_faster_solutions(*_1) }.reduce(&:*)
end

def part2(races)
  race = races.transpose.map { _1.map(&:to_s).reduce(&:+).to_i }
  total_faster_solutions(*race)
end

data = parse("./inputs/example_06.txt")
puts(part1(data))
puts(part2(data))
