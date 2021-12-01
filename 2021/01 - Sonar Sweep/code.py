"""
Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1
"""
import operator


def fetch_data(path: str) -> list[int]:
    with open(path) as f:
        return list(map(int, f.read().splitlines()))


def part_1(data: list[int]) -> int:
    "Count all increasing measurements in a list."
    return sum(map(operator.lt, data, data[1:]))


def part_2(data: list[int]) -> int:
    "Count all increasing measuements in a three-wide sliding window."
    window: list[int] = list(map(sum, zip(data, data[1:], data[2:])))
    return part_1(window)


def main():
    data: list[int] = fetch_data("example.txt")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
