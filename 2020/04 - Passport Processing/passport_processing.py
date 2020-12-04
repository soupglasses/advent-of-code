from pprint import pprint
from functools import partial
import re

FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

RE_HAIR_COLOR = re.compile('^#[0-9a-f]{6}$')
RE_PID = re.compile('^[0-9]{9}$')

with open('input.txt', 'r') as f:
    raw_passports = f.read()

def parse_passport(raw_passport: str) -> dict:
    return dict(field.split(':') for field in raw_passport.split())

def parse_passports(raw_passports: str) -> list[dict]:
    return [parse_passport(raw_passport)
            for raw_passport in raw_passports.split('\n\n')]

def validate_year_range(year: str, low: str, high: str) -> bool:
    return low <= year <= high

def validate_height(height: str) -> bool:
    measure, height = height[-2:], height[:-2]
    if measure == 'cm':
        return '150' <= height <= '193'
    if measure == 'in':
        return '59' <= height <= '76'

def validate_hair_color(color: str) -> bool:
    return bool(RE_HAIR_COLOR.match(color))

def validate_eye_color(color: str) -> bool:
    return color in VALID_EYE_COLORS

def validate_pid(pid: str) -> bool:
    return bool(RE_PID.match(pid))

def validate_cid(cid) -> bool:
    return True

validate_fields = {
    'byr': partial(validate_year_range, low='1920', high='2002'),
    'iyr': partial(validate_year_range, low='2010', high='2020'),
    'eyr': partial(validate_year_range, low='2020', high='2030'),
    'hgt': validate_height,
    'hcl': validate_hair_color,
    'ecl': validate_eye_color,
    'pid': validate_pid,
    'cid': validate_cid,
}

def check_passport_fields(passport: dict, fields: set) -> bool:
    return all(rule in passport for rule in fields)

def passport_validation(passport: dict, fields: set) -> bool:
    return (
        check_passport_fields(passport, fields)
        and all(validate_fields[key](value) for key, value in passport.items())
    )

if __name__ == '__main__':
    passports = parse_passports(raw_passports)
    print('A1:', sum(check_passport_fields(passport, FIELDS)
                     for passport in passports))

    print('A2:', sum(passport_validation(passport, FIELDS)
                     for passport in passports))
