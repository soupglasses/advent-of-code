import re

pattern = re.compile(
    '(?P<low>^\d+)-(?P<high>\d+) (?P<letter>\w+): (?P<secret>.+)'
)

with open('input.txt', 'r') as f:
    passwords = []
    for line in f.read().splitlines():
        match = re.match(pattern, line)
        passwords.append(match.groupdict())

def valid_password_by_chars(password: dict) -> bool:
    low, high = int(password['low']), int(password['high'])
    letter, secret = password['letter'], password['secret']
    
    return low <= secret.count(letter) <= high

def valid_password_by_pos(password: dict) -> bool:
    low, high = int(password['low']) - 1, int(password['high']) - 1
    letter, secret = password['letter'], password['secret']

    return (secret[low] == letter) != (secret[high] == letter)

print("Q1:", "How many passwords are valid according to their policies?")
print("A1:", sum(valid_password_by_chars(password) for password in passwords))

print("Q2:", "How many passwords are valid according to the new",
      "interpretation of the policies?")
print("A2:", sum(valid_password_by_pos(password) for password in passwords))
