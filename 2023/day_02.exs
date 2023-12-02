#!/usr/bin/env elixir

defmodule Day02 do
  @moduledoc """
  Day 2 - Cube Conundrum

  Part 1:
    Given a set of game records with cube subsets, determine which games would be
    possible if the bag had 12 red, 13 green, and 14 blue cubes.
    Find the sum of the IDs of those possible games.

  Part 2:
    Now, determine the minimum cubes required for each game to be possible.
    Find the product of these minimums for each game and sum them together.
  """

  def parser(game_records) do
    Map.new(
      String.split(game_records, "\n", trim: true)
      |> Enum.map(fn "Game " <> game ->
        {id, ": " <> rest} = Integer.parse(game)

        plays =
          rest
          |> String.split("; ")
          |> Enum.map(fn cubes ->
            String.split(cubes, ", ")
            |> Map.new(fn cube ->
              {amount, " " <> color} = Integer.parse(cube)
              {color, amount}
            end)
          end)

        {id, plays}
      end)
    )
  end

  def part1(games) do
    Map.filter(games, fn {_, game} ->
      Enum.all?(game, fn hand ->
        Map.get(hand, "red", 0) <= 12 &&
          Map.get(hand, "green", 0) <= 13 &&
          Map.get(hand, "blue", 0) <= 14
      end)
    end)
    |> Map.keys()
    |> Enum.sum()
  end

  def part2(games) do
    Enum.map(games, fn {_, game} ->
      Enum.reduce(game, [0, 0, 0], fn item, acc ->
        [
          max(Map.get(item, "red", 0), Enum.at(acc, 0)),
          max(Map.get(item, "green", 0), Enum.at(acc, 1)),
          max(Map.get(item, "blue", 0), Enum.at(acc, 2))
        ]
      end)
      |> Enum.reduce(&*/2)
    end)
    |> Enum.sum()
  end
end

game_records_data = File.read!("inputs/example_02.txt")
games = Day02.parser(game_records_data)

IO.inspect(Day02.part1(games))
IO.inspect(Day02.part2(games))
