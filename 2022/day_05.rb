#!/usr/bin/env ruby

path = ARGV[0] || File.join(__dir__, "inputs", "example_05.txt")

crate_stacks, move_commands = File.read(path)
  .split("\n\n")
  .map { _1.split("\n") }

# Creates a zero-indexed crate stack
# Example Input:
# [" [C]     ",
#  " [A] [B] ",
#  "  1   2  "]
# Output:
# [ ["A", "C"], ["B"] ]
crate_stacks = crate_stacks
  .map(&:chars)
  .transpose
  .map { _1.join.strip }
  .filter { _1.match?(/\d/) }
  .map { _1[0..-2].chars.reverse }

# Creates a list of move commands that are zero indexed.
# Example Input:
# ["move 10 from 1 to 2", "move 2 from 3 to 1"]
# Output:
# [[10, 0, 1], [2, 2, 0]]
move_commands = move_commands
  .map {
  _1
    .match(/move (\d+) from (\d) to (\d)/)
    .captures
    .map(&:to_i)
    .map.with_index { |d, i|
    i == 0 ? d : d - 1
  }
}

def run_crane(crate_stacks, move_commands, strategy)
  stack = crate_stacks.map(&:clone)

  move_commands.each do |amount, from, to|
    stack[from]
      .pop(amount)
      .send(strategy)
      .then { stack[to].concat _1 }
  end

  stack.map(&:last).join
end

def part_1(crate_stacks, move_commands)
  run_crane(crate_stacks, move_commands, :reverse)
end

def part_2(crate_stacks, move_commands)
  run_crane(crate_stacks, move_commands, :itself)
end

puts part_1(crate_stacks, move_commands)
puts part_2(crate_stacks, move_commands)
