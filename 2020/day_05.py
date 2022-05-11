import sys
from typing import Optional

BP_BINARY = str.maketrans('FLBR', '0011')


def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = raw.splitlines()
    return data


def seat_pos(board_pass: str) -> int:
    return int(board_pass.translate(BP_BINARY), 2)

def seat_id(board_pass: str) -> int:
    row, col = seat_pos(board_pass[:7]), seat_pos(board_pass[7:])
    return row * 8 + col

def find_missing(lst: list) -> int:
    return next(i for i in range(min(lst), max(lst) + 1) if i not in lst)


if __name__ == '__main__':
    boarding_passes = parse_data("inputs/example_05.txt")

    taken_seat_ids = [seat_id(board_pass) for board_pass in boarding_passes]

    print('Q1:', 'What is the highest seat ID on a boarding pass?')
    print('A1:', max(taken_seat_ids))

    print('Q2:', 'What is the ID of your seat?')
    print('A2:', find_missing(taken_seat_ids))
