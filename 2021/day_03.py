"""
Day 3: Binary Diagnostic

https://adventofcode.com/2021/day/3
"""
from collections import Counter
from itertools import count
from typing import Optional

Data = list[str]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = raw
    return data


def most_common(iterable):
    occurences = Counter(iterable).most_common(2)
    if occurences[0][1] == occurences[1][1]:
        # Bias towrads the higher value
        return sorted(map(lambda x: x[0], occurences), reverse=True)[0]
    return occurences[0][0]


def least_common(iterable):
    occurences = Counter(iterable).most_common()
    if occurences[0][1] == occurences[1][1]:
        # Bias towards the lower value
        return sorted(map(lambda x: x[0], occurences))[0]
    return occurences[-1][0]


def reduce_by_repeating(func, data: Data) -> Optional[str]:
    """
    Will reduce by repeadedly filtering on a given function till a
    single value remains.

    If the filtering removes all items from the list, return None.
    """
    if not data:
        return None

    width = len(data[0])
    for i in count():
        if len(data) <= 1:
            return next(iter(data), None)

        pos = i % width
        vertical_line = list(zip(*data))[pos]
        filter_value = func(vertical_line)
        data = [item for item in data if item[pos] == filter_value]

    raise Exception("How did you get down here?")


def part_1(data: Data):
    """
    Use the binary numbers in your diagnostic report to calculate the
    gamma rate and epsilon rate, then multiply them together. What is
    the power consumption of the submarine?
    """
    gamma = int("".join(map(most_common, zip(*data))), base=2)
    epsilon = int("".join(map(least_common, zip(*data))), base=2)
    return gamma * epsilon


def part_2(data: Data):
    """
    Use the binary numbers in your diagnostic report to calculate the
    oxygen generator rating and CO2 scrubber rating, then multiply
    them together. What is the life support rating of the submarine?
    """
    oxygen = int(reduce_by_repeating(most_common, data) or "0", base=2)
    co2 = int(reduce_by_repeating(least_common, data) or "0", base=2)

    return oxygen * co2


def main():
    data = parse_file("inputs/example_03.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
