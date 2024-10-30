#!/usr/bin/env ruby

class Day09
  def initialize(input)
    @points = input.split("\n").map { |line| line.split.map(&:to_i) }
  end

  def derivative_from_differences(points)
    # Computes the derivative of a unknown function from its sequence of points.
    # F: {2, 4, 6, ..., n} -> F': {2, 2, 2, ..., n-1}
    # This implementation is only an estimate of the real derivate, and is particularly prone
    # to accumulate error for non-linear functions.
    # However, it's used since AoC generated the answers using this particular derivative function.
    points.each_cons(2).map { |a, b| b - a }
  end

  def next_in_sequence(sequence)
    # Base case: If all elements are the same, the rate of change is zero, and no further derivatives exist.
    return sequence.first if sequence.uniq.length == 1
    # Recursive case: Otherwise, find the next derivative and add the last element to it.
    next_in_sequence(derivative_from_differences(sequence)) + sequence.last
  end

  def prev_in_sequence(sequence)
    next_in_sequence(sequence.reverse)
  end

  def part1
    @points.map { |history| next_in_sequence(history) }.sum
  end

  def part2
    @points.map { |history| prev_in_sequence(history) }.sum
  end
end

answer = Day02.new(File.open("2023/inputs/example_09.txt").read)
puts answer.part1
puts answer.part2
