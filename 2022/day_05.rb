#!/usr/bin/env ruby

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_05.txt")

MoveCommand = Struct.new(:amount, :from, :to)

# Creates a zero-indexed crate stack.
#
# @param raw_crate_stacks [String] The AoC, seperated by newlines.
# @return [Array<Array<String>>] Array with zero-indexed crate-stacks.
# @example Stack where stack 1 holds crate A and C, while stack 2 holds crate B.
#   parse_raw_crate_stacks(" [C]     \n [A] [B] \n  1   2  ") #=> [["A", "C"], ["BC"]]
def parse_raw_crate_stacks(raw_crate_stacks)
  raw_crate_stacks
    .split("\n")
    .map(&:chars)
    .transpose
    .map { _1.join.strip }
    .filter { _1.match?(/\d/) }
    .map { _1[0..-2].chars.reverse }
end

# Returns array of MoveCommands that are zero indexed.
#
# @param raw_move_commands [String] The AoC input, seperated by newlines.
# @return [Array<MoveCommand>] An array of MoveCommand's.
# @example Move 2 crates from stack 3 to stack 1.
#   parse_raw_move_commands("move 2 from 3 to 1") #=> [<struct MoveCommand amount=2, from=2, to=0>]
def parse_raw_move_commands(raw_move_commands)
  raw_move_commands
    .split("\n")
    .map { |line|
    line
      .match(/move (\d+) from (\d) to (\d)/)
      .captures
      .map(&:to_i)
      .map.with_index { |number, index| index == 0 ? number : number - 1 }
      .then { MoveCommand.new(_1, _2, _3) }
  }
end

#  Runs the AoC crane trough a crate stack following a set strategy.
#
# @param crate_stacks [Array<Array<String>>] zero-indexed crate stacks.
# @param move_commands [Array<MoveCommand>] zero-indexed MoveCommand's.
# @param strategy [Symbol] The array symbol to use for each move command.
# @return [String] string containing the top-crate from each stack.
def run_crane(crate_stacks, move_commands, strategy)
  stack = crate_stacks.map(&:clone)

  move_commands.each do |move|
    stack[move.from]
      .pop(move.amount)
      .send(strategy)
      .then { stack[move.to].concat _1 }
  end

  stack.map(&:last).join
end

def part_1(crate_stacks, move_commands)
  run_crane(crate_stacks, move_commands, :reverse)
end

def part_2(crate_stacks, move_commands)
  run_crane(crate_stacks, move_commands, :itself)
end


def main()
  raw_crate_stacks, raw_move_commands = File.read(PATH)
    .split("\n\n")

  crate_stacks = parse_raw_crate_stacks(raw_crate_stacks)
  move_commands = parse_raw_move_commands(raw_move_commands)

  puts part_1(crate_stacks, move_commands)
  puts part_2(crate_stacks, move_commands)
end

main()
