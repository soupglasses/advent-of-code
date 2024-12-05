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
      return false if !d.zero? && dir != d
    end
    true
  end

  # Divides the enumerable into three parts: elements before, current element, and elements after.
  # Yields each partition to the block.
  #
  # @example
  #   [1,2,3].partitions.to_a  #=> [[[], 1, [2, 3]], [[1], 2, [3]], [[1, 2], 3, []]]
  #
  # @yieldparam left [Array] The elements before the current element.
  # @yieldparam current [Object] The current element.
  # @yieldparam right [Array] The elements after the current element.
  # @return [Enumerator] if no block is given.
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
  # Returns the middle element(s) of the array.
  # If the array has an odd size, returns an array with one element.
  # If the array has an even size, returns an array with two elements.
  # If the array is empty, returns itself.
  #
  # @return [Array] the middle element(s).
  def middle
    return self if empty?

    size.odd? ? self[size / 2, 1] : self[(size / 2) - 1, 2]
  end
end
