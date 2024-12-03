#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'

class Day03 < AoCDay
  def setup(data)
    @data = data
  end

  def part1
    @data
      .scan(/mul\((\d{1,3}),(\d{1,3})\)/)
      .sum { _1.to_i * _2.to_i }
  end

  def part2
    @data
      .scan(/(?:don't\(\).*?do\(\))|mul\((\d{1,3}),(\d{1,3})\)/m)
      .sum { _1.to_i * _2.to_i }
  end
end
