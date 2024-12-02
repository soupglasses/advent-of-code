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

  def initialize(data = nil)
    setup data if data
  end

  def setup(data)
    raise NotImplementedError
  end

  def self.new_from_dynamic_file(type, nth)
    input_file_name = "#{type}_#{day}#{nth ? "_#{nth}" : ''}.txt"
    source_location = new.method(:setup).source_location.first
    new(
      Pathname.new(source_location)
        .dirname
        .join('../inputs', input_file_name)
        .read
    )
  end

  def self.new_from_example_file(nth = nil)
    new_from_dynamic_file(:example, nth)
  end

  def self.new_from_input_file
    new_from_dynamic_file(:input, nil)
  end

  def self.run
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

  def self.finalize
    run if caller.last.match?(%r{/day_\d\d\.rb:})
  end

  def self.inherited(base)
    TracePoint.trace(:end) do |t|
      if base == t.self
        base.finalize
        t.disable
      end
    end
  end
end
