# frozen_string_literal: true

module Enumerable
  # Checks if the given enumerable is a non-strict monotonic sequence.
  #
  # @return [Boolean] `true` if the enumerable is monotonic, `false` otherwise.
  #
  # @example
  #   [1, 2, 3].monotonic?  # => true
  #   [3, 2, 1].monotonic?  # => true
  #   [1, 1, 1].monotonic?  # => true
  #   [1, 3, 2].monotonic?  # => false
  def monotonic?
    dir = 0
    each_cons(2) do |a, b|
      d = b <=> a
      dir = d if dir.zero?
      return false if dir != d unless d.zero?
    end
    true
  end

  def partitions
    return enum_for(:partitions) unless block_given?

    each_with_index do |current, index|
      left = take(index)
      right = drop(index + 1)
      yield [left, current, right]
    end
  end
end

class Array
  def middle
    return nil if empty?
    size.odd? ? self[size / 2] : self[(size / 2) - 1, 2]
  end
end
