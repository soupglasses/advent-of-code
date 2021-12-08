#!/usr/bin/env python3.10
"""
Day 8: Seven Segment Search

https://adventofcode.com/2021/day/8
"""

Data = list[list[list[str]]]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = list(map(lambda x: [a.split(" ") for a in x.split(" | ")], raw))
    return data


def decode_num(positions: list[str], display: list[str]) -> int:
    segments = {len(val): set(val) for val in positions}
    number = ""
    for encoded_number in map(set, display):
        match (
           # Toal unique lit cells in the 7 segment display
           len(encoded_number),
           # Count of lit cells that share a position with the number 4
           len(encoded_number & segments[4]),
           # Count of lit cells that share a position with the number 1
           len(encoded_number & segments[2]),
        ):
           case 2, _, _: number += "1"
           case 3, _, _: number += "7"
           case 4, _, _: number += "4"
           case 7, _, _: number += "8"
           case 5, 2, _: number += "2"
           case 5, 3, 1: number += "5"
           case 5, 3, 2: number += "3"
           case 6, 4, _: number += "9"
           case 6, 3, 1: number += "6"
           case 6, 3, 2: number += "0"
    return int(number)


def part_1(data: Data) -> int:
    """
    In the output values, how many times do digits 1, 4, 7, or 8
    appear?
    """
    count = 0
    for _, display in data:
        for number in display:
            # Check if the displayed number is 1, 4, 7, or 8.
            if len(set(number)) in (2, 4, 3, 7):
                count += 1
    return count


def part_2(data: Data) -> int:
    """
    For each entry, determine all of the wire/segment connections and
    decode the four-digit output values. What do you get if you add up
    all of the output values?
    """
    count = 0
    for positions, display in data:
        count += decode_num(positions, display)
    return count


def main():
    data = parse_file("inputs/input_08.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
