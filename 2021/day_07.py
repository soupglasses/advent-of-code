"""
Day 7: Treachery of Whales

https://adventofcode.com/2021/day/7
"""

Data = list[int]


def parse_file(path: str) -> Data:
    with open(path) as f:
        raw = f.read().splitlines()
        data = sorted(list(map(int, raw[0].split(","))))
    return data


def calculate_cost(data: Data, pos: int) -> int:
    cost = 0
    for point in data:
        # fuel spent is the same as distance travelled
        cost += abs(point - pos)

    return cost


def calculate_cost_2(data: Data, pos: int) -> int:
    # TODO: Find a way to add this into a single calculate_cost function.
    cost = 0
    for point in data:
        # fuel spent is the triangle number of the distance
        steps = abs(point - pos)
        cost += (steps ** 2 + steps) // 2

    return cost


def part_1(data: Data):
    """
    Determine the horizontal position that the crabs can align to using
    the least fuel possible so they can make you an escape route! How
    much fuel must they spend to align to that position?
    """
    # Now both part one and two are extremely inefficient. As im just
    # bruteforcing all possible posisions on the curve before doing a
    # min scan over that. I could easily implement an algorithmn or
    # similar that would see when it each side becomes more expensive
    # and return the lowest number it can find. But im short on time
    # for today, and the 2nd part only really takes a second to run
    # this way. So its not *needed* to do.
    positions = [calculate_cost(data, pos) for pos in range(len(data))]
    return min(positions)


def part_2(data: Data):
    """
    Determine the horizontal position that the crabs can align to using
    the least fuel possible. How much fuel must they spend to align to
    that position?
    """
    positions = [calculate_cost_2(data, pos) for pos in range(len(data))]
    return min(positions)


def main():
    data = parse_file("inputs/input_07.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
