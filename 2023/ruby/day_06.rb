#!/usr/bin/env ruby

require_relative '../../aocday'

class Day06 < AoCDay
  def setup(input)
    @races = parse(input.split("\n"))
  end

  def parse(lines)
    race_times = lines.first.sub(/^Time:\s*/, '').split.map(&:to_i)
    race_distances = lines.last.sub(/^Distance:\s*/, '').split.map(&:to_i)
    race_times.zip(race_distances)
  end

  def next_digit(float)
    float % 1 == 0.0 ? float.to_i + 1 : float.ceil
  end

  def prev_digit(float)
    -next_digit(-float)
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

  def part1
    @races.map { |(time, distance)| total_faster_solutions(time, distance) }.reduce(:*)
  end

  def part2
    time, distance = @races.transpose.map { _1.join.to_i }
    total_faster_solutions(time, distance)
  end
end
