#!/usr/bin/env elixir

defmodule Day01 do
  @moduledoc """
  Day 1 - Trebuchet?!

  Part 1:
    Recover calibration values from a document by keeping the first and last
    digit found in each line. Sum all the two-digit numbers.

  Part 2:
    Extends part 1 by also including the overlapping spelled-out digits as
    possible valid digits.
  """

  def parse_digit_only(""), do: []
  def parse_digit_only(<<c>> <> rest) when c in ?0..?9, do: [c - ?0 | parse_digit_only(rest)]
  def parse_digit_only(<<_>> <> rest), do: parse_digit_only(rest)

  def parse_both(""), do: []
  def parse_both(<<c>>   <> rest) when c in ?0..?9, do: [c - ?0 | parse_both(rest)]
  def parse_both("zero"  <> rest), do: [0 | parse_both("o" <> rest)]
  def parse_both("one"   <> rest), do: [1 | parse_both("e" <> rest)]
  def parse_both("two"   <> rest), do: [2 | parse_both("o" <> rest)]
  def parse_both("three" <> rest), do: [3 | parse_both("e" <> rest)]
  def parse_both("four"  <> rest), do: [4 | parse_both("r" <> rest)]
  def parse_both("five"  <> rest), do: [5 | parse_both("e" <> rest)]
  def parse_both("six"   <> rest), do: [6 | parse_both("x" <> rest)]
  def parse_both("seven" <> rest), do: [7 | parse_both("n" <> rest)]
  def parse_both("eight" <> rest), do: [8 | parse_both("t" <> rest)]
  def parse_both("nine"  <> rest), do: [9 | parse_both("e" <> rest)]
  def parse_both(<<_>>   <> rest), do: parse_both(rest)

  def recalibrate_by(strategy, document) do
    String.split(document)
    |> Enum.map(strategy)
    |> Enum.map(fn digits -> List.first(digits) * 10 + List.last(digits) end)
    |> Enum.sum()
  end

  def part1(document), do: recalibrate_by(&parse_digit_only/1, document)
  def part2(document), do: recalibrate_by(&parse_both/1, document)
end

part_1_document = File.read!("../inputs/example_01_1.txt")
part_2_document = File.read!("../inputs/example_01_2.txt")

IO.inspect(Day01.part1(part_1_document))
IO.inspect(Day01.part2(part_2_document))
