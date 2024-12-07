#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'
require_relative '../../std++'

class Day07 < AoCDay
  def setup(data)
    @evaluations = data.lines.map { _1.scan(/\d+/).map(&:to_i) }
  end

  def can_fit?(target, numbers, concat: false)
    *remaining, n = numbers
    return n == target if remaining.empty?

    # Multiply
    return true if (target % n).zero? && can_fit?(target / n, remaining, concat)
    # Concat
    return true if concat && target.end_with?(n) && can_fit?(target / (10**n.length), remaining, concat)

    # Sum
    can_fit?(target - n, remaining, concat)
  end

  def part1
    @evaluations.select { |total, *numbers| can_fit?(total, numbers) }.sum(&:first)
  end

  def part2
    @evaluations.select { |total, *numbers| can_fit?(total, numbers, concat: true) }.sum(&:first)
  end
end
