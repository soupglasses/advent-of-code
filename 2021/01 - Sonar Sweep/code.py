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
    """
    How many measurements are larger than the previous measurement?
    """
    return sum(map(operator.lt, data, data[1:]))


def part_2(data: Data) -> int:
    """
    Consider sums of a three-measurement sliding window. How many sums
    are larger than the previous sum?
    """
    # Since the the sliding windows are built up as `a + b + c < b + c + d`,
    # we can take out `b` and `c` from both sides. Ending up with a simple
    # `a < d` comparison.
    return sum(map(operator.lt, data, data[3:]))


def main():
    data = parse_file("example.txt")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))


if __name__ == "__main__":
    main()
