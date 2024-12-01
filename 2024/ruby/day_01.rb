#!/usr/bin/env ruby

require_relative 'aocday'

class Day01 < AoCDay
  def initialize(data)
    @lists = data.split("\n").map { _1.split.map(&:to_i) }
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
      .reduce { |left, right|  left.sum { |number, count| number * count * right[number].to_i } }
  end
end

Day01.cli
