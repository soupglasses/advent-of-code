#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'

class Day03 < AoCDay
  def setup(data)
    @data = data
  end

  def sum_uncorrupted_mults(data)
    data
      .scan(/mul\((\d{1,3}),(\d{1,3})\)/)
      .sum { _1.to_i * _2.to_i }
  end

  def part1
    sum_uncorrupted_mults @data
  end

  def part2
    sum_uncorrupted_mults @data.gsub(/don't\(\).*?(?:do\(\)|\Z)/m, "")
  end
end
