import re

pattern = re.compile(r'(^\d+)-(\d+) (\w): (.+)', re.MULTILINE)


def valid_password_by_letters(low: int, high: int,
                              letter: str, password: str) -> bool:
    return low <= password.count(letter) <= high

def valid_password_by_pos(low: int, high: int,
                          letter: str, password: str) -> bool:
    return (password[low-1] == letter) != (password[high-1] == letter)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        passwords = pattern.findall(f.read())

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
