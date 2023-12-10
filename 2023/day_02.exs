#!/usr/bin/env elixir

Mix.install([
  {:nimble_parsec, "~> 1.0"}
])

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

  def part1(games) do
    {:ok, parsed, "", _, _, _} = Day02.Parser.from_string(games)

    Enum.filter(parsed, fn {:game, game} ->
      Keyword.get_values(game, :round)
      |> Enum.all?(fn round ->
        Keyword.get(round, :red, 0) <= 12 &&
          Keyword.get(round, :green, 0) <= 13 &&
          Keyword.get(round, :blue, 0) <= 14
      end)
    end)
    |> Enum.map(fn {:game, game} -> Keyword.get(game, :id) end)
    |> Enum.sum()
  end

  def part2(games) do
    {:ok, parsed, "", _, _, _} = Day02.Parser.from_string(games)

    Enum.map(parsed, fn {:game, game} ->
      Keyword.get_values(game, :round)
      |> Enum.reduce([0, 0, 0], fn item, acc ->
        [
          max(Keyword.get(item, :red, 0), Enum.at(acc, 0)),
          max(Keyword.get(item, :green, 0), Enum.at(acc, 1)),
          max(Keyword.get(item, :blue, 0), Enum.at(acc, 2))
        ]
      end)
      |> Enum.product()
    end)
    |> Enum.sum()
  end
end

defmodule Day02.Parser do
  import NimbleParsec

  hand = fn color ->
    integer(min: 1)
    |> ignore(string(" "))
    |> ignore(string(color))
    |> unwrap_and_tag(String.to_atom(color))
  end

  round =
    times(
      concat(
        choice([hand.("red"), hand.("green"), hand.("blue")]),
        ignore(optional(string(", ")))
      ),
      min: 1
    )
    |> ignore(optional(string("; ")))
    |> tag(:round)

  game =
    ignore(string("Game "))
    |> integer(min: 1)
    |> unwrap_and_tag(:id)
    |> ignore(string(": "))
    |> times(round, min: 1)
    |> tag(:game)

  games =
    repeat(
      concat(
        game,
        ignore(optional(string("\n")))
      )
    )

  defparsec(:from_string, games)
end

game_records_data = File.read!("inputs/example_02.txt")

IO.inspect(Day02.part1(game_records_data))
IO.inspect(Day02.part2(game_records_data))
