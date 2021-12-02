"""
Day 2:

https://adventofcode.com/2021/day/2
"""

Data = list[tuple[str, int]]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = map(str.split, raw)
        data = map(lambda x: (x[0], int(x[1])), data)
    return list(data)


def part_1(data: Data):
    """
    What do you get if you multiply your final horizontal position by
    your final depth?
    """
    distance, depth = 0, 0
    for direction, amount in data:
        if direction == "forward":
            distance += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    return distance * depth


def part_2(data: Data):
    """
    What do you get if you multiply your final horizontal position by
    your final depth?
    """
    distance, aim, depth = 0, 0, 0
    for direction, amount in data:
        if direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        elif direction == "forward":
            distance += amount
            depth += aim * amount
    return distance * depth


def main():
    data = parse_file("example.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
