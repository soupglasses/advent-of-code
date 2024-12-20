#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'
require_relative '../../std++'

class Day02 < AoCDay
  def setup(data)
    @reports = data.lines.map { _1.split.map(&:to_i) }
  end

  def reactor_safety(report)
    return false unless report.monotonic?

    report
      .each_cons(2)
      .all? { (_2 - _1).abs.between?(1, 3) }
  end

  def part1
    @reports.count { reactor_safety _1 }
  end

  def part2
    @reports.count { |report| report.combination(report.length - 1).any? { reactor_safety _1 } }
  end
end
