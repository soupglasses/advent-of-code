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

  def parse(""), do: []
  def parse(<<c>>   <> rest) when c in ?0..?9, do: [c - ?0 | parse(rest)]
  def parse("zero"  <> rest), do: [0 | parse("o" <> rest)]
  def parse("one"   <> rest), do: [1 | parse("e" <> rest)]
  def parse("two"   <> rest), do: [2 | parse("o" <> rest)]
  def parse("three" <> rest), do: [3 | parse("e" <> rest)]
  def parse("four"  <> rest), do: [4 | parse("r" <> rest)]
  def parse("five"  <> rest), do: [5 | parse("e" <> rest)]
  def parse("six"   <> rest), do: [6 | parse("x" <> rest)]
  def parse("seven" <> rest), do: [7 | parse("n" <> rest)]
  def parse("eight" <> rest), do: [8 | parse("t" <> rest)]
  def parse("nine"  <> rest), do: [9 | parse("e" <> rest)]
  def parse(<<_>>   <> rest), do: parse(rest)

  def solve(str, func) do
    String.split(str)
    |> Enum.map(func)
    |> Enum.map(fn digits -> List.first(digits) * 10 + List.last(digits) end)
    |> Enum.sum()
  end

  def part1(str), do: solve(str, &parse_digit_only/1)
  def part2(str), do: solve(str, &parse/1)
end

part_1_data = File.read!("./inputs/example_01_1.txt")
part_2_data = File.read!("./inputs/example_01_2.txt")

IO.inspect(Day01.part1(part_1_data))
IO.inspect(Day01.part2(part_2_data))
