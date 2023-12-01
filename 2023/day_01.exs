#!/usr/bin/env elixir

{:ok, re_num} = Regex.compile("(?=(\\d|one|two|three|four|five|six|seven|eight|nine))")
nums = %{one: "1", two: "2", three: "3", four: "4", five: "5", six: "6", seven: "7", eight: "8", nine: "9"}

number_to_digit = fn
  <<c>> when ?0 <= c and c <= ?9 -> c
  item -> Map.fetch!(nums, String.to_atom(item))
end

# TODO: Rework this to work on strings directly.

solver = fn data -> String.split(data, "\n", trim: true)
  |> Enum.map(fn line ->
    Regex.scan(re_num, line, capture: :all_but_first)
    |> List.flatten()
    |> Enum.map(number_to_digit)
    |> Kernel.then(fn x -> [List.first(x), List.last(x)] end)
    |> List.to_string()
    |> String.to_integer()
  end)
  |> Enum.reduce(&Kernel.+/2)
end

part_1_data = File.read!("./inputs/example_01a.txt")
part_2_data = File.read!("./inputs/example_01b.txt")

IO.inspect solver.(part_1_data)
IO.inspect solver.(part_2_data)
