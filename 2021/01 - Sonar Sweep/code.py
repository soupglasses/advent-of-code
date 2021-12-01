"""
Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1
"""
import operator

Data = list[int]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = list(map(int, raw))
    return data


def part_1(data: Data) -> int:
    "Count all increasing measurements in a list."
    return sum(map(operator.lt, data, data[1:]))


def part_2(data: Data) -> int:
    "Count all increasing measuements in a three-wide sliding window."
    return sum(map(operator.lt, data, data[3:]))


def main():
    data = parse_file("example.txt")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
