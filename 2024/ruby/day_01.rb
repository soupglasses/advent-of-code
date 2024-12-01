#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'

class Day01 < AoCDay
  def setup(data)
    @lists =
      data
      .scan(/(\d+)\s+(\d+)/)
      .map { |left, right| [left.to_i, right.to_i] }
  end

  def part1
    @lists
      .transpose.map(&:sort).transpose
      .sum { (_2 - _1).abs }
  end

  def part2
    @lists
      .transpose
      .map(&:tally)
      .reduce do |left_col, right_col|
        left_col.sum { |number, count| number * count * right_col.fetch(number, 0) }
      end
  end
end

Day01.run_if_main
