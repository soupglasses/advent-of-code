import re
import sys
from functools import partial
from typing import Optional 

FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

RE_HAIR_COLOR = re.compile('^#[0-9a-f]{6}$')
RE_PID = re.compile('^[0-9]{9}$')


def parse_passport(raw_passport: str) -> dict:
    return dict(field.split(':') for field in raw_passport.split())


def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = [parse_passport(raw_passport)
            for raw_passport in raw.split('\n\n')]
    return data


def validate_year(year: str, low: int, high: int) -> bool:
    return low <= int(year) <= high

def validate_height(height: str) -> bool:
    unit, height = height[-2:], height[:-2]
    if unit == 'cm':
        return 150 <= int(height) <= 193
    elif unit == 'in':
        return 59 <= int(height) <= 76
    return False

def validate_hair_color(color: str) -> bool:
    return bool(RE_HAIR_COLOR.match(color))

def validate_eye_color(color: str) -> bool:
    return color in VALID_EYE_COLORS

def validate_pid(pid: str) -> bool:
    return bool(RE_PID.match(pid))

def validate_cid(cid: str) -> bool:
    return True


validate_fields = {
    'byr': partial(validate_year, low=1920, high=2002),
    'iyr': partial(validate_year, low=2010, high=2020),
    'eyr': partial(validate_year, low=2020, high=2030),
    'hgt': validate_height,
    'hcl': validate_hair_color,
    'ecl': validate_eye_color,
    'pid': validate_pid,
    'cid': validate_cid,
}


def check_fields(passport: dict) -> bool:
    return all(field in passport for field in FIELDS)

def validate_passport(passport: dict) -> bool:
    return (
        check_fields(passport) and all(
            validate_fields[field](value)
            for field, value in passport.items()
        )
    )


if __name__ == '__main__':
    passports = parse_data("inputs/example_04.txt")

    print('Q1:', 'In your batch file, how many passports are valid?',
          'Treat cid as optional.')
    print('A1:', sum(check_fields(passport)
                     for passport in passports))

    print('Q2:', 'In your batch file, how many passports have the required',
          'fields and valid values?')
    print('A2:', sum(validate_passport(passport)
                     for passport in passports))
