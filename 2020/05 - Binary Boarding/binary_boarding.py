
with open('input.txt', 'r') as f:
    raw_seats = f.read().splitlines()

def get_row(f: str):
    if 'F' in f or 'B' in f:
        lim = (0, 127)
    else:
        lim = (0, 7)
    for step in f:
        split = sum(lim) / len(lim)
        if step == 'F' or step == 'L':
            lim = (lim[0], int(split))
        else:
            lim = (int(split) + 1, lim[1])
    return lim[0]

def get_seat(b: str):
    b_row, b_col = b[:7], b[7:]
    row, col = get_row(b_row), get_row(b_col)
    return row, col

def get_seat_id(b: str):
    row, col = get_seat(b)
    return row * 8 + col

def find_missing(lst: list):
    return [x for x in range(lst[0], lst[-1]+1)
                             if x not in lst][0]

if __name__ == '__main__':
    taken_seats = [get_seat_id(id_) for id_ in raw_seats]
    print('A1:', max(taken_seats))
    print('A2:', find_missing(sorted(taken_seats)))
