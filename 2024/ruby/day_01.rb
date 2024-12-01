#!/usr/bin/env ruby

require_relative 'aocday'

class Day01 < AoCDay
  def initialize(data)
    @lists = data
      .scan(/(\d+)\s+(\d+)/)
      .map { |left, right| [left.to_i, right.to_i] }
  end

  def part1
    @lists
      .transpose.map(&:sort).transpose
      .map { (_2 - _1).abs }.sum
  end

  def part2
    @lists
      .transpose
      .map(&:tally)
      .reduce { |left, right|  left.sum { |number, count| number * count * right.fetch(number, 0) } }
  end
end

Day01.run_if_main
