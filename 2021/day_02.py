#!/usr/bin/env python3
"""
Day 2: Dive

https://adventofcode.com/2021/day/2
"""

Data = list[tuple[str, int]]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = [(direction, int(amount)) for direction, amount in map(str.split, raw)]
    return data


def plotter(data: Data) -> tuple[int, int, int]:
    """
    Finds the end position for a given list of directions.

    Returns:
        A 3-integer tuple corresponding to the end positions calculated
        by the inputted data, where:

        x: is the distance travelled on the x axis
        y_1: is the distance travelled on the flipped y axis
        y_2: is the flipped y axis calculated by the aim method
            described in part 2
    """
    x, y_1, y_2 = 0, 0, 0
    for direction, amount in data:
        if direction == "up":
            y_1 -= amount
        elif direction == "down":
            y_1 += amount
        elif direction == "forward":
            x += amount
            y_2 += y_1 * amount
    return x, y_1, y_2


def part_1(data: Data) -> int:
    """
    Calculate the horizontal position and depth you would have after
    following the planned course. What do you get if you multiply your
    final horizontal position by your final depth?
    """
    distance, depth, _ = plotter(data)
    return distance * depth


def part_2(data: Data) -> int:
    """
    Using this new interpretation of the commands, calculate the
    horizontal position and depth you would have after following the
    planned course. What do you get if you multiply your final
    horizontal position by your final depth?
    """
    distance, _, depth = plotter(data)
    return distance * depth


def main():
    data = parse_file("inputs/example_02.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
