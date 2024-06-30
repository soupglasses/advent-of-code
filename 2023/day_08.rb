#!/usr/bin/env ruby

def parse(lines)
  directions = lines.first.chars.map { _1 == "R" ? 1 : 0 }
  table = lines.drop(2).each_with_object({}) do |line, hash|
    hash[line[0..2]] = [line[7..9], line[12..14]]
  end
  [directions, table]
end

def steps_to_match(directions, table, start, goal)
  current, step = start, 0
  until current.end_with?(goal)
    current = table[current][directions[step % directions.size]]
    step += 1
  end
  step
end

def part1(directions, table)
  steps_to_match(directions, table, "AAA", "ZZZ")
end

def part2(directions, table)
  table.keys
    .select { _1.end_with?("A") }
    .map { |start| steps_to_match(directions, table, start, "Z") }
    .reduce(&:lcm)
end

directions, table = parse(File.readlines("./inputs/example_08.txt", chomp: true))
puts part1(directions, table)
puts part2(directions, table)
