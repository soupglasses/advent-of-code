import re

pattern = re.compile(
    '(?P<min>^\d+)-(?P<max>\d+) (?P<letter>\w+): (?P<secret>.+)'
)

with open('input.txt', 'r') as f:
    passwords = []
    for line in f.read().splitlines():
        match = re.match(pattern, line)
        passwords.append(match.groupdict())

def valid_password_by_chars(password: dict) -> bool:
    min_, max_ = int(password['min']), int(password['max'])
    letter, secret = password['letter'], password['secret']
    
    return min_ <= secret.count(letter) <= max_

def valid_password_by_pos(password: dict) -> bool:
    min_, max_ = int(password['min']) - 1, int(password['max']) - 1
    letter, secret = password['letter'], password['secret']

    return (secret[min_] == letter) != (secret[max_] == letter)

print("Q1:", "How many passwords are valid according to their policies?")
print("A1:", sum(valid_password_by_chars(password) for password in passwords))

print("Q2:", "How many passwords are valid according to the new",
      "interpretation of the policies?")
print("A2:", sum(valid_password_by_pos(password) for password in passwords))
