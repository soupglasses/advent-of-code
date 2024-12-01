require 'pathname'

class AoCDay
  def self.day
    # Extracts the day from the class name.
    name[/\d+/]
  end

  def self.load_dynamic_file(type, n)
    file_name = "#{type}_#{day}" + (n ? "_#{n}" : "") + ".txt"
    self.new(
      Pathname.new(__FILE__)
        .dirname
        .join("../inputs", file_name)
        .read
    )
  end

  def self.example_file(n = nil)
    self.load_dynamic_file(:example, n)
  end

  def self.input_file
    self.load_dynamic_file(:input, nil)
  end

  def self.cli
    if ENV.fetch("AOC_ATTEMPT", "false") == "true"
      day = input_file
    else
      day = example_file
    end
    puts day.part1
    puts day.part2
  end
end
