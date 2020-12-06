from math import prod

SLOPES = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def count_trees(grid: list, right: int, down: int) -> int:
    trees = 0
    width, height = len(grid[0]), len(grid)
    for pos in range(0, height, down):
        hit = grid[pos][pos * right // down % width]
        if hit == '#':
            trees += 1
    return trees

def prod_from_slopes(grid: list, slopes: list) -> int:
    return prod(count_trees(grid, right, down) for right, down in slopes)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid_map = f.read().splitlines()

    print('Q1:', 'Starting at the top-left corner of your map and following',
          'a slope of right 3 and down 1, how many trees would you encounter?')
    print('A1:', count_trees(grid_map, 3, 1))

    print('Q2:', 'What do you get if you multiply together the number of',
          'trees encountered on each of the listed slopes?')
    print('A2:', prod_from_slopes(grid_map, SLOPES))
