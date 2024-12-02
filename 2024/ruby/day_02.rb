#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'
require_relative '../../std++'

class Day02 < AoCDay
  def setup(data)
    @reports = data.lines.map { _1.split.map(&:to_i) }
  end

  def reactor_safety(report)
    changes = report.each_cons(2).map { _2 - _1 }
    changes.all? { _1.abs.between(1, 3) } && changes.monotonic?
  end

  def part1
    @reports.count { reactor_safety(_1) }
  end

  def part2
    @reports.count { _1.combination(_1.length - 1).any?(&method(:reactor_safety)) }
  end
end

Day02.run_if_main
