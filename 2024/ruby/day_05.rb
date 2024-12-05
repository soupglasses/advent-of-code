#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'
require_relative '../../std++'

class Day05 < AoCDay
  def setup(data)
    rules, updates = data.split("\n\n")

    @comes_after =
      rules
      .lines
      .map { |line| line.split("|").map(&:to_i) }
      .group_by(&:first)
      .transform_values { |values| values.flat_map(&:last) }

    @updates = updates.lines.map { |line| line.split(",").map(&:to_i) }
  end

  def valid?(line)
    line.partitions.all? do |left, current, _|
      left.all? { @comes_after[_1]&.include?(current) }
    end
  end

  def sort(line)
    line.sort { |l, r| @comes_after[l]&.include?(r) ? 1 : -1 }
  end

  def part1
    @updates.select { valid? _1 }.sum { _1.middle.first }
  end

  def part2
    @updates.reject { valid? _1 }.sum { (sort _1).middle.first }
  end
end
