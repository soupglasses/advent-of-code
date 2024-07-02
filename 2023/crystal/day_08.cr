#!/usr/bin/env crystal

alias Directions = Array(UInt8)
alias Table = Hash(String, Tuple(String, String))

def parse(lines : Array(String)) : {Directions, Table}
  directions = lines.first.chars.map { |c| (c == 'R') ? 1_u8 : 0_u8 }
  table = lines.skip(2).each_with_object(Table.new) do |line, hash|
    hash[line[0, 3]] = {line[7, 3], line[12, 3]}
  end
  {directions, table}
end

def steps_to_match(directions : Directions, table : Table, start : String, goal : String) : UInt32
  current, step = start, 0_u32
  until current.ends_with?(goal)
    current = table[current][directions[step % directions.size]]
    step += 1
  end
  step
end

def part1(directions : Directions, table : Table) : UInt32
  steps_to_match(directions, table, "AAA", "ZZZ")
end

def part2(directions : Directions, table : Table) : UInt64
  table.keys
    .select { |key| key.ends_with?("A") }
    .map { |start| steps_to_match(directions, table, start, "Z") }
    .reduce(1_u64) { |acc, count| acc.lcm(count) }
end

directions, table = parse(File.read_lines("../inputs/example_08.txt"))
puts part1(directions, table)
puts part2(directions, table)
