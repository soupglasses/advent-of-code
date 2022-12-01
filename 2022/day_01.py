#!/usr/bin/env python3
"""
Day 01:

https://adventofcode.com/2022/day/1
"""
import sys

DAY = "01"
Data = list[list[int]]


def parse_data() -> Data:
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        path = f"inputs/example_{DAY}.txt"

    with open(path, encoding="utf-8") as f:
        raw = f.read()

    data = [
        [int(line or "0") for line in lines.split("\n")] for lines in raw.split("\n\n")
    ]
    return data


def part_1(data: Data):
    return max(sum(group) for group in data)


def part_2(data: Data):
    return sum(sorted((sum(group) for group in data), reverse=True)[:3])


def main():
    data = parse_data()

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
