#!/usr/bin/env python3
"""
Day 04: Ceres Search

https://adventofcode.com/2024/day/4
"""
import sys
import os

import numpy as np
from scipy.signal import convolve2d


DAY = "04"

DIRECTIONS = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1),  # Left
    (-1, 1),  # Up-right
    (1, 1),  # Down-right
    (1, -1),  # Down-left
    (-1, -1),  # Up-left
]


def parse_data(file):
    return np.array([[ord(char) for char in line] for line in file.splitlines()])


def find_xmas_patterns(matrix):
    rows, cols = matrix.shape
    matches = []

    for row in range(rows):
        for col in range(cols):
            for d_row, d_col in DIRECTIONS:
                if 0 <= row + 3 * d_row < rows and 0 <= col + 3 * d_col < cols:
                    sequence = "".join(map(chr, matrix[row + np.arange(4) * d_row, col + np.arange(4) * d_col]))
                    if sequence == "XMAS":
                        matches.append((row, col, (d_row, d_col)))

    return matches


def find_x_mas_patterns(matrix):
    # Avoid accidental matches with f.x. ord("X") == 89, only choose primes after ord("Z") == 90:
    kernel = np.array([
        [101,  0, 103],  # M . S
        [  0, 97,   0],  # . A .
        [103,  0, 101],  # M . S
    ])

    # The X-MAS pattern encoded using prime numbers.
    x_mas_sum = (
        97 * ord("A")
        + (101 * ord("M") + 101 * ord("S"))
        + (103 * ord("M") + 103 * ord("S"))
    )

    convolved = convolve2d(matrix, kernel, mode="same")

    return np.argwhere(convolved == x_mas_sum)


def part_1(data):
    return len(find_xmas_patterns(data))


def part_2(data):
    return len(find_x_mas_patterns(data))


def cli():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    elif os.getenv("AOC_ATTEMPT") in ["true", "yes", "y", "1", "on"]:
        path = f"../inputs/input_{DAY}.txt"
    else:
        path = f"../inputs/example_{DAY}.txt"

    with open(path, encoding="utf-8") as f:
        data = parse_data(f.read())

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    cli()
