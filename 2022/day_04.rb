#!/usr/bin/env ruby

PATH = ARGV[0] || File.join(__dir__, "inputs", "example_04.txt")

class Range
  def disjoint?(other)
    not self.intersect?(other)
  end

  def intersect?(other)
    # Uses `self.max` to support exclusive ranges correctly.
    return true if self.begin <= other.begin && other.begin <= self.max
    return true if other.begin <= self.begin && self.begin <= other.max
  end

  def intersection(other)
    return nil if self.disjoint?(other)
    Range.new([self.begin, other.begin].max, [self.max, other.max].min)
  end

  alias_method :&, :intersection
end

camp_assignment_pairs = File.read(PATH).chomp.split("\n")
  .map { |section_pair|
  section_pair
    .split(/,|-/)
    .map(&:to_i)
    .each_slice(2)
    .map { Range.new(_1, _2) }
}

def part_1(data)
  data.count { _1.cover?(_2) || _2.cover?(_1) }
end

def part_2(data)
  data.count { _1.intersect?(_2) }
end

puts part_1(camp_assignment_pairs)
puts part_2(camp_assignment_pairs)
