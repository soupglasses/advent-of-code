#!/usr/bin/env ruby

GAME = {
  "A X" => [1 + 3, 3 + 0],
  "A Y" => [2 + 6, 1 + 3],
  "A Z" => [3 + 0, 2 + 6],
  "B X" => [1 + 0, 1 + 0],
  "B Y" => [2 + 3, 2 + 3],
  "B Z" => [3 + 6, 3 + 6],
  "C X" => [1 + 6, 2 + 0],
  "C Y" => [2 + 0, 3 + 3],
  "C Z" => [3 + 3, 1 + 6],
}

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_02.txt")

game_rounds = File.read(PATH).split("\n")

def part_1(data)
  data.map { GAME[_1][0] }.sum
end

def part_2(data)
  data.map { GAME[_1][1] }.sum
end

puts part_1(game_rounds)
puts part_2(game_rounds)
