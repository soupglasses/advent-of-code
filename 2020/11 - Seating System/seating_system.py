NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1))


def get_neighbours_simple(i: int, y: int, lst: list):
    tmp = ""
    height, width = len(lst), len(lst[i])
    for ni, ny in NEIGHBOURS:
        if 0 <= i + ni < height and 0 <= y + ny < width:
            tmp += lst[i + ni][y + ny]
        else:
            tmp += '.'
    return tmp

def get_neighbours_advanced(i: int, y: int, lst: list):
    tmp = ""
    height, width = len(lst), len(lst[i])
    for ni, ny in NEIGHBOURS:
        nix, nyx = ni, ny
        while True:
            if not (0 <= i + ni < height and 0 <= y + ny < width):
                tmp += '.'
                break
            if lst[i + ni][y + ny] == '#':
                tmp += '#'
                break
            elif lst[i + ni][y + ny] == 'L':
                tmp += 'L'
                break
            else:
                ni, ny = nix + ni, nyx + ny
    return tmp

def stepper(seating: list, tolerance: int):
    step = []
    for i, line in enumerate(seating):
        step.append([])
        for y, char in enumerate(line):
            if char in 'L#':
                if tolerance <= 4:
                    around = get_neighbours_simple(i, y, seating).count('#')
                else:
                    around = get_neighbours_advanced(i, y, seating).count('#')

                if char == 'L' and around == 0:
                    step[i].append('#')
                elif char == '#' and around >= tolerance:
                    step[i].append('L')
                else:
                    step[i].append(char)
            else:
                step[i].append(char)
    return step

def find_equilibrium_str(seating: list, tolerance: int) -> str:
    a = stepper(seating, tolerance)
    b = []
    while a != b:
        b = a
        a = stepper(a, tolerance)
    return '\n'.join([''.join(line) for line in a])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        seats = [list(line) for line in f.read().splitlines()]

    print('A1:', find_equilibrium_str(seats, 4).count('#'))

    print('A2:', find_equilibrium_str(seats, 5).count('#'))
