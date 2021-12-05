"""
Day 5: Hydrothermal Venture

https://adventofcode.com/2021/day/5
"""
import numpy as np

Data = np.ndarray


def coords_to_tuple(bytes_: bytes) -> tuple[int, ...]:
    # bytes given as 'latin1' from numpy.loadtxt
    return tuple(int(i) for i in bytes_.decode("latin1").split(","))


def parse_file(path: str) -> Data:
    return np.loadtxt(
        path,
        converters={0: coords_to_tuple, 1: coords_to_tuple},
        dtype=int,
        delimiter=" -> ",
    )


def plot_line_low(x_0: int, y_0: int, x_1: int, y_1: int) -> list[tuple[int, int]]:
    d_x = x_1 - x_0
    d_y = y_1 - y_0
    y_i = 1
    if d_y < 0:
        y_i = -1
        d_y = -d_y
    D = (2 * d_y) - d_x
    y = y_0

    res = []
    for x in range(x_0, x_1 + 1):
        res.append((x, y))
        if D > 0:
            y = y + y_i
            D = D + (2 * (d_y - d_x))
        else:
            D = D + 2 * d_y
    return res


def plot_line_high(x_0: int, y_0: int, x_1: int, y_1: int) -> list[tuple[int, int]]:
    d_x = x_1 - x_0
    d_y = y_1 - y_0
    x_i = 1
    if d_x < 0:
        x_i = -1
        d_x = -d_x
    D = (2 * d_x) - d_y
    x = x_0

    res = []
    for y in range(y_0, y_1 + 1):
        res.append((x, y))
        if D > 0:
            x = x + x_i
            D = D + (2 * (d_x - d_y))
        else:
            D = D + 2 * d_x
    return res


def plot_line(x_0: int, y_0: int, x_1: int, y_1: int) -> list[tuple[int, int]]:
    """
    Python implementation of the Bresenham's line algorithm.

    https://en.wikipedia.org/wiki/Bresenham's_line_algorithm
    """
    if abs(y_1 - y_0) < abs(x_1 - x_0):
        if x_0 > x_1:
            return plot_line_low(x_1, y_1, x_0, y_0)
        return plot_line_low(x_0, y_0, x_1, y_1)
    if y_0 > y_1:
        return plot_line_high(x_1, y_1, x_0, y_0)
    return plot_line_high(x_0, y_0, x_1, y_1)


def plot_intercetions(data: Data) -> np.ndarray:
    max_size = int(data.max()) + 1
    diagram = np.zeros((max_size, max_size), dtype=int)

    for ((x_0, y_0), (x_1, y_1)) in data:
        points = plot_line(x_0, y_0, x_1, y_1)
        for x, y in points:
            diagram[y][x] += 1

    return diagram


def part_1(data: Data) -> int:
    """
    Consider only horizontal and vertical lines. At how many points do
    at least two lines overlap?
    """
    # I can probably find a numpy command to do this, but i am still a beginner
    # to numpy as a libary. So im just using list comprehension for filtering.
    filtered_data = np.array(
        [((a, b), (c, d)) for ((a, b), (c, d)) in data if a == c or b == d],
        dtype=int,
    )

    return (plot_intercetions(filtered_data) > 1).sum()


def part_2(data: Data):
    """
    Consider all of the lines. At how many points do at least two lines
    overlap?
    """
    return (plot_intercetions(data) > 1).sum()


def main():
    data = parse_file("inputs/input_05.txt")

    print("Part 1", part_1(data))
    print("Part 2", part_2(data))


if __name__ == "__main__":
    main()
