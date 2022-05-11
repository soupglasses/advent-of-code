import re
import sys
from typing import Optional 


PATTERN = re.compile(r'(^\d+)-(\d+) (\w): (.+)', re.MULTILINE)

def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = PATTERN.findall(raw)
    return data


def valid_password_by_letters(low: int, high: int,
                              letter: str, password: str) -> bool:
    return low <= password.count(letter) <= high

def valid_password_by_pos(low: int, high: int,
                          letter: str, password: str) -> bool:
    return (password[low-1] == letter) != (password[high-1] == letter)


if __name__ == '__main__':
    passwords = parse_data("inputs/example_02.txt")

    print("Q1:", "How many passwords are valid according to their policies?")
    print("A1:", sum(
        valid_password_by_letters(int(low), int(high), letter, password)
        for low, high, letter, password in passwords
    ))

    print("Q2:", "How many passwords are valid according to the new",
          "interpretation of the policies?")
    print("A2:", sum(
        valid_password_by_pos(int(low), int(high), letter, password)
        for low, high, letter, password in passwords
    ))
