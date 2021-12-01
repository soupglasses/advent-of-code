"""
Day $:

https://adventofcode.com/2021/day/$
"""

Data = list


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = raw
    return data


def part_1(data: Data):
    ...


def part_2(data: Data):
    ...


def main():
    data = parse_file("example.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
