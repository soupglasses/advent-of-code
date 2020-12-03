from math import prod

with open('input.txt', 'r') as f:
    grid_map = f.read().splitlines()

a = 0
for line_nr, coord_nr in zip(range(0, len(grid_map), 1), range(0, 100_000_000, 3)):
    hit = grid_map[line_nr % len(grid_map)][coord_nr % len(grid_map[0])]
    if hit == '#':
        a += 1
print('A1:', a)

total = []
for right, down in ((1,1), (3,1), (5,1), (7,1), (1,2)):
    a = 0
    for line_nr, coord_nr in zip(range(0, len(grid_map), down), range(0, 100_000_000, right)):
        hit = grid_map[line_nr % len(grid_map)][coord_nr % len(grid_map[0])]
        if hit == '#':
            a += 1
    total.append(a)
print('A2:', prod(total))
