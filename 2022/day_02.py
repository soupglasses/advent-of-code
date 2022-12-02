#!/usr/bin/env python3
"""
Day 02:

https://adventofcode.com/2022/day/2
"""
import sys

DAY = "02"
Data = list[str]

GAME = {
    "A X": [1 + 3, 3 + 0],
    "A Y": [2 + 6, 1 + 3],
    "A Z": [3 + 0, 2 + 6],
    "B X": [1 + 0, 1 + 0],
    "B Y": [2 + 3, 2 + 3],
    "B Z": [3 + 6, 3 + 6],
    "C X": [1 + 6, 2 + 0],
    "C Y": [2 + 0, 3 + 3],
    "C Z": [3 + 3, 1 + 6],
}

if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    path = f"inputs/example_{DAY}.txt"


def parse_data() -> Data:
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    data = raw.strip().split("\n")

    return data


def part_1(data: Data):
    return sum(GAME[round][0] for round in data)


def part_2(data: Data):
    return sum(GAME[round][1] for round in data)


def main():
    data = parse_data()

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
