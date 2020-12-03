from math import prod

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open('input.txt', 'r') as f:
    grid_map = f.read().splitlines()

def count_trees(grid: list, right: int, down: int) -> int:
    trees = 0
    width, height = len(grid[0]), len(grid)
    for pos in range(0, height, down):
        hit = grid[pos][pos * right // down % width]
        if hit == '#':
            trees += 1
    return trees

def prod_of_slopes(grid: list, slopes: list) -> int:
    return prod(count_trees(grid, right, down) for right, down in slopes)

print('A1:', count_trees(grid_map, 3, 1))
print('A2:', prod_of_slopes(grid_map, SLOPES))
