bp_binary = str.maketrans('FLBR', '0011')


def seat_pos(board_pass: str) -> int:
    return int(board_pass.translate(bp_binary), 2)

def seat_id(board_pass: str) -> int:
    row, col = seat_pos(board_pass[:7]), seat_pos(board_pass[7:])
    return row * 8 + col

def find_missing(lst: list) -> int:
    return next(i for i in range(lst[0], lst[-1]+1) if i not in lst)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        boarding_passes = f.read().splitlines()

    taken_seat_ids = [seat_id(board_pass) for board_pass in boarding_passes]

    print('Q1:', 'What is the highest seat ID on a boarding pass?')
    print('A1:', max(taken_seat_ids))

    print('Q2:', 'What is the ID of your seat?')
    print('A2:', find_missing(sorted(taken_seat_ids)))
