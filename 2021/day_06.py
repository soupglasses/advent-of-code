"""
Day 6: Lanternfish

https://adventofcode.com/2021/day/6
"""

Data = list[int]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = list(map(int, raw[0].split(",")))
    return data


def growth_over(data: Data, days: int) -> int:
    # We keep a total count of all fish and how many days left they
    # each are from reproducing, represented by their position in the
    # list. Also making space for newborns at the end of the list.
    fishes = [data.count(i) for i in range(9)]
    for _ in range(days):
        # Take the amount of fish at "day 0" out of our list.
        reproducing_fish = fishes.pop(0)
        # Add them back in to "day 6" as fish live forever.
        fishes[6] += reproducing_fish
        # Add the new fish that were born to "day 8".
        fishes.append(reproducing_fish)

    return sum(fishes)


def part_1(data: Data):
    """
    Find a way to simulate lanternfish. How many lanternfish would
    there be after 80 days?
    """
    return growth_over(data, days=80)

def part_2(data: Data) -> int:
    """
    How many lanternfish would there be after 256 days?
    """
    return growth_over(data, days=256)


def main():
    data = parse_file("inputs/input_06.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
