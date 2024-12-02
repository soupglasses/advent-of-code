# frozen_string_literal: true

module Enumerable
  # Checks if the enumerable is monotonic (either entirely non-increasing or non-decreasing).
  #
  # @return [Boolean] `true` if the enumerable is monotonic, `false` otherwise.
  #
  # @example
  #   [1, 2, 3].monotonic?  # => true
  #   [3, 2, 1].monotonic?  # => true
  #   [1, 3, 2].monotonic?  # => false
  def monotonic?
    dir = 0
    each_cons(2) do |a, b|
      d = b <=> a
      dir = d unless d.zero?
      return false if dir != d && !d.zero?
    end
    true
  end
end
