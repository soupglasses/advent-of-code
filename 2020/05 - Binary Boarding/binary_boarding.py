
with open('input.txt', 'r') as f:
    boarding_passes = f.read().splitlines()

def parse_seat_pos(board_pass: str):
    limit = (0, 2 ** len(board_pass) - 1)
    for step in board_pass:
        split = sum(limit) // 2
        lower, upper = limit
        if step in 'FL':
            limit = (lower, split)
        else:
            limit = (split+1, upper)
    return limit[0]

def seat_pos(board_pass: str):
    bp_row, bp_col = board_pass[:7], board_pass[7:]
    row, col = parse_seat_pos(bp_row), parse_seat_pos(bp_col)
    return row, col

def seat_id(board_pass: str):
    row, col = seat_pos(board_pass)
    return row * 8 + col

def find_missing(lst: list):
    return next((x for x in range(lst[0], lst[-1]+1) if x not in lst))

if __name__ == '__main__':
    taken_seat_ids = [seat_id(board_pass) for board_pass in boarding_passes]
    print('A1:', max(taken_seat_ids))
    print('A2:', find_missing(sorted(taken_seat_ids)))
