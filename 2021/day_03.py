#!/usr/bin/env python3
"""
Day 3: Binary Diagnostic

https://adventofcode.com/2021/day/3
"""
import sys
from typing import Optional, Union

Data = list[str]

def parse_data(path: Optional[str]) -> Data:
    if not sys.stdin.isatty():
        raw = sys.stdin.readlines()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.readlines()
        else:
            sys.exit("No stdin data was recived.")

    data = raw
    return data


def most_common(text: Union[str, tuple[str, ...]]) -> str:
    ones, zeros = text.count("1"), text.count("0")
    if ones >= zeros:
        return "1"
    return "0"


def least_common(text: Union[str, tuple[str, ...]]) -> str:
    return "0" if most_common(text) == "1" else "1"


def transpose(lst: list) -> list:
    return list(zip(*lst))


def reduce_on(func, data: Data, pos: int = 0) -> str:
    """
    Will reduce by repeadedly filtering on a given function till a
    single value remains.

    If the filtering removes all items from the list, return None.
    """
    if not data:
        raise Exception(
            "Data is empty, cannot return " +
            "(filter might have removed all values?)"
        )
    if len(data) == 1:
        return data[0]

    filter_val = func(str(transpose(data)[pos]))
    return reduce_on(
        func,
        [a for a in data if a[pos] == filter_val],
        (pos + 1) % len(data[0])
    )


def part_1(data: Data):
    """
    Use the binary numbers in your diagnostic report to calculate the
    gamma rate and epsilon rate, then multiply them together. What is
    the power consumption of the submarine?
    """
    gamma = int("".join(map(most_common, transpose(data))), base=2)
    epsilon = int("".join(map(least_common, transpose(data))), base=2)
    return gamma * epsilon


def part_2(data: Data):
    """
    Use the binary numbers in your diagnostic report to calculate the
    oxygen generator rating and CO2 scrubber rating, then multiply
    them together. What is the life support rating of the submarine?
    """
    oxygen = int(reduce_on(most_common, data), base=2)
    co2 = int(reduce_on(least_common, data), base=2)

    return oxygen * co2


def main():
    data = parse_data("inputs/example_03.txt")

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
