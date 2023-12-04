#!/usr/bin/env elixir

Mix.install([
  {:nimble_parsec, "~> 1.0"}
])

defmodule Day04 do
  def parse(records) do
    {:ok, parsed, "", _, _, _} = Day04.Parser.from_string(records)

    Enum.map(parsed, fn {:game, game} ->
      {
        game[:id],
        MapSet.intersection(
          MapSet.new(game[:winning_numbers]),
          MapSet.new(game[:hand])
        )
        |> Enum.count()
      }
    end)
  end

  def part1(records) do
    card_count_wins = parse(records)

    card_count_wins
    |> Enum.map(&(:math.pow(2, elem(&1, 1) - 1) |> Kernel.floor()))
    |> Enum.sum()
  end

  def part2(records) do
    card_count_wins = parse(records)
    original_cards = Map.new(card_count_wins, &{elem(&1, 0), 1})

    card_count_wins
    |> Enum.reduce(original_cards, fn {id, count}, acc ->
      Range.new(id + 1, id + count, 1)
      |> Enum.reduce(%{}, fn i, iacc ->
        Map.merge(iacc, %{i => Map.get(acc, id, 1)})
      end)
      |> Map.merge(acc, fn _k, v1, v2 -> v1 + v2 end)
    end)
    |> Map.values()
    |> Enum.sum()
  end
end

defmodule Day04.Parser do
  import NimbleParsec

  round = fn type ->
    times(
      ignore(optional(string(" ")))
      |> integer(min: 1, max: 2)
      |> ignore(optional(string(" "))),
      min: 1
    )
    |> tag(type)
  end

  game =
    ignore(string("Card"))
    |> ignore(times(string(" "), min: 1))
    |> integer(min: 1)
    |> unwrap_and_tag(:id)
    |> ignore(string(": "))
    |> concat(round.(:winning_numbers))
    |> ignore(string("| "))
    |> concat(round.(:hand))
    |> tag(:game)
    |> ignore(optional(string("\n")))

  games = repeat(game)

  defparsec(:from_string, games)
end

data = File.read!("./inputs/example_04.txt")

IO.inspect(Day04.part1(data))
IO.inspect(Day04.part2(data))
