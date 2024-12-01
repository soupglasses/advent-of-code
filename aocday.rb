# frozen_string_literal: true

require 'pathname'

# AoCDay is a base class designed for handling Advent of Code (AoC) challenges.
# It abstracts the process of loading input and example data, and provides
# a standardized structure for solving challenge tasks part 1 and part 2.
class AoCDay
  def self.day
    # Extracts the day from the class name.
    name[/\d+/]
  end

  def initialize(data)
    setup data
  end

  def setup(data)
    raise NotImplementedError
  end

  def self.new_from_dynamic_file(type, nth)
    file_name = "#{type}_#{day}#{nth ? "_#{nth}" : ''}.txt"
    caller_path = caller.last.split(':').first
    new(
      Pathname.new(caller_path)
        .dirname
        .join('../inputs', file_name)
        .read
    )
  end

  def self.new_from_example_file(nth = nil)
    new_from_dynamic_file(:example, nth)
  end

  def self.new_from_input_file
    new_from_dynamic_file(:input, nil)
  end

  def self.run_if_main
    return if caller.any? { |line| line.include?('require') }

    day_part2 = nil

    if %w[true yes y 1 on].include? ENV['AOC_ATTEMPT']
      day = new_from_input_file
    else
      begin
        day = new_from_example_file
      rescue Errno::ENOENT
        day = new_from_example_file(1)
        day_part2 = new_from_example_file(2)
      end
    end

    day_part2 ||= day

    puts day.part1
    puts day_part2.part2
  end
end
