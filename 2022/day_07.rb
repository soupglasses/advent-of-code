#!/usr/bin/env ruby

require 'pathname'

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_07.txt")

terminal_output = File.read(PATH).chomp

class FileNode

  FOLDER = "folder"
  FILE = "file"

  attr_reader :type, :path, :size

  def initialize(type, path, size = 0)
    @type = type
    @path = path
    @size = size
  end

  def self.from_terminal_output(terminal_output)
    commands = terminal_output.split("\n")
    paths = commands
      # We have to make our own scan left function here.
      .each_with_object([Pathname.new("")]) do |command, acc|
        if command.start_with?("$ cd ")
          acc << acc.last / command[5..]
        elsif command.start_with?("dir ")
          acc << acc.last / command[4..]
        else
          acc << acc.last
        end
      end
      .drop(1)

    paths.zip(commands)
      .reject { |_, command| command.start_with?("$") }
      .map do |path, command|
        if command.start_with?("dir ")
          self.new(self::FOLDER, path, 0)
        elsif command.start_with?(/\d/)
          size, file_name = command.split(" ")
          self.new(self::FILE, path / file_name, size.to_i)
        else
          raise "unknown command: #{command}"
        end
      end
  end
end

def part_1(data)
end

def part_2(data)
end

puts FileNode.from_terminal_output(terminal_output)
