#!/usr/bin/env elixir

defmodule Day01 do
  def parse(""), do: []
  def parse(<<c>> <> rest) when c in ?0..?9, do: [c - ?0 | parse(rest)]
  def parse("zero" <> rest),  do: [0 | parse("o" <> rest)]
  def parse("one" <> rest),   do: [1 | parse("e" <> rest)]
  def parse("two" <> rest),   do: [2 | parse("o" <> rest)]
  def parse("three" <> rest), do: [3 | parse("e" <> rest)]
  def parse("four" <> rest),  do: [4 | parse("r" <> rest)]
  def parse("five" <> rest),  do: [5 | parse("e" <> rest)]
  def parse("six" <> rest),   do: [6 | parse("x" <> rest)]
  def parse("seven" <> rest), do: [7 | parse("n" <> rest)]
  def parse("eight" <> rest), do: [8 | parse("t" <> rest)]
  def parse("nine" <> rest),  do: [9 | parse("e" <> rest)]
  def parse(<<_>> <> rest),   do: parse(rest)

  def solve(str) do
    String.split(str)
    |> Enum.map(&Day01.parse/1)
    |> Enum.map(fn digits -> List.first(digits) * 10 + List.last(digits) end)
    |> Enum.sum()
  end
end

part_1_data = File.read!("./inputs/example_01a.txt")
part_2_data = File.read!("./inputs/example_01b.txt")

IO.inspect Day01.solve(part_1_data)
IO.inspect Day01.solve(part_2_data)
