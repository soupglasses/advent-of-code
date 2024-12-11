#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative '../../aocday'
require_relative '../../std++'

class Day11 < AoCDay
  def setup(data)
    @items = data.split(' ').map(&:to_i)
  end

  def blink(item, blinks_left)
    ((@blink_memo ||= {})[item] ||= {})[blinks_left] ||= begin
      return 1 if blinks_left.zero?
      return blink(1, blinks_left - 1) if item.zero?

      if item.length.even?
        left, right = item.divmod(10**(item.length / 2))

        blink(left, blinks_left - 1) + blink(right, blinks_left - 1)
      else
        blink(item * 2024, blinks_left - 1)
      end
    end
  end

  def part1
    @items.sum { blink(_1, 25) }
  end

  def part2
    @items.sum { blink(_1, 75) }
  end
end
