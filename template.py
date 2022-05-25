"""
Day $:

https://adventofcode.com/2021/day/$
"""
import sys
from typing import Optional

Data = list[str]

def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = raw
    return data


def part_1(data: Data):
    ...


def part_2(data: Data):
    ...


def main():
    data = parse_data("inputs/example_$.txt")

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
