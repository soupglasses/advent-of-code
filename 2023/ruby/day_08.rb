#!/usr/bin/env ruby

require_relative '../../aocday'

class Day08 < AoCDay
  def setup(input)
    @directions, @table = parse(input.split("\n"))
  end

  def parse(lines)
    directions = lines.first.chars.map { { 'R' => 1, 'L' => 0 }[_1] }
    table = lines.drop(2).each_with_object({}) do |line, table|
      table[line[0...3]] = [line[7...10], line[12...15]]
    end
    [directions, table]
  end

  def steps_to_match(start, desired_end)
    current, steps = start, 0
    until current.end_with?(desired_end)
      current = @table[current][@directions[steps % @directions.size]]
      steps += 1
    end
    steps
  end

  def part1
    steps_to_match('AAA', 'ZZZ')
  end

  def part2
    @table.keys
      .select { _1.end_with?('A') }
      .map { |start| steps_to_match(start, 'Z') }
      .reduce(&:lcm)
  end
end
