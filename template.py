#!/usr/bin/env python3
"""
Day 00:

https://adventofcode.com/2021/day/00
"""
import sys

DAY = "00"
Data = list[str]


def parse_data() -> Data:
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        path = f"inputs/example_{DAY}.txt"

    with open(path, encoding="utf-8") as f:
        raw = f.read()

    data = raw
    return data


def part_1(data: Data):
    ...


def part_2(data: Data):
    ...


def main():
    data = parse_data()

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
