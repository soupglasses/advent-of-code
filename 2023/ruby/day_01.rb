#!/usr/bin/env ruby

require_relative '../../aocday'

class Day01 < AoCDay
  WORD_TO_INTEGER = {
    'zero' => 0, 'one' => 1, 'two' => 2, 'three' => 3,
    'four' => 4, 'five' => 5, 'six' => 6, 'seven' => 7,
    'eight' => 8, 'nine' => 9,
  }

  def setup(data)
    @lines = data.split("\n")
  end

  def extract_calibration_value_v1(line)
    line
      .gsub(/\D/, '')
      .chars.values_at(0, -1)
      .join.to_i
  end

  def extract_calibration_value_v2(line)
    line
      .scan(/(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))/)
      .map { |match| to_word_i(match.first) }
      .values_at(0, -1)
      .join.to_i
  end

  def part1
    @lines.map { |line| extract_calibration_value_v1(line) }.sum
  end

  def part2
    @lines.map { |line| extract_calibration_value_v2(line) }.sum
  end

  private

  def to_word_i(string)
    WORD_TO_INTEGER[string] || string.to_i
  end
end
