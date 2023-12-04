#!/usr/bin/env elixir

Mix.install([
  {:nimble_parsec, "~> 1.0"}
])

defmodule Day04 do
  def parse_card_wins(records) do
    {:ok, parsed, "", _, _, _} = Day04.Parser.from_string(records)

    Enum.map(parsed, fn {:game, game} ->
      {
        game[:id],
        MapSet.new(game[:winning_numbers])
        |> MapSet.intersection(MapSet.new(game[:numbers_we_have]))
        |> MapSet.size()
      }
    end)
  end

  def part1(records) do
    parse_card_wins(records)
    |> Enum.map(&floor(2 ** (elem(&1, 1) - 1)))
    |> Enum.sum()
  end

  def part2(records) do
    card_wins = parse_card_wins(records)
    original_cards = Map.new(card_wins, &{elem(&1, 0), 1})

    Enum.reduce(card_wins, original_cards, fn {id, count}, acc ->
      Range.new(id + 1, id + count, 1)
      |> Enum.reduce(%{}, fn i, iacc ->
        Map.put(iacc, i, Map.get(acc, id, 1))
      end)
      |> Map.merge(acc, fn _, v1, v2 -> v1 + v2 end)
    end)
    |> Map.values()
    |> Enum.sum()
  end
end

defmodule Day04.Parser do
  import NimbleParsec

  number =
    ignore(optional(string(" ")))
    |> integer(min: 1, max: 2)
    |> ignore(optional(string(" ")))

  numbers = fn type ->
    times(number, min: 1)
    |> tag(type)
  end

  game =
    ignore(string("Card"))
    |> ignore(times(string(" "), min: 1))
    |> integer(min: 1)
    |> unwrap_and_tag(:id)
    |> ignore(string(": "))
    |> concat(numbers.(:winning_numbers))
    |> ignore(string("| "))
    |> concat(numbers.(:numbers_we_have))
    |> tag(:game)
    |> ignore(optional(string("\n")))

  games = repeat(game)

  defparsec(:from_string, games)
end

data = File.read!("./inputs/example_04.txt")

IO.inspect(Day04.part1(data))
IO.inspect(Day04.part2(data))
