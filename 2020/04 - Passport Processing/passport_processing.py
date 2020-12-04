from pprint import pprint
import re

naive_rules = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

rules = {
    'byr': {'low': 1920, 'high': 2002},
    'iyr': {'low': 2010, 'high': 2020},
    'eyr': {'low': 2020, 'high': 2030},
    'hgt': {'cm': {'low': 150, 'high': 193},
            'in': {'low': 59, 'high': 76}},
    'hcl': {'re': '^#[0-9a-f]{6}$'},
    'ecl': {'cl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']},
    'pid': {'re': '^[0-9]{9}$'},
    'cid': {},
}

with open('input.txt', 'r') as f:
    raw_passports = f.read()

def is_int(value):
    try: 
        int(value)
        return True
    except ValueError:
        return False

def parse_passport(raw_passport: str) -> dict:
    passport = {}
    for t in raw_passport.replace('\n', ' ').split():
        key, value = t.split(':')
        passport[key] = value
    return passport

def parse_passports(raw_passports: str) -> list[dict]:
    passports = []
    for raw_passport in raw_passports.split('\n\n'):
        passports.append(parse_passport(raw_passport))
    return passports

def naive_passport_validation(passport: dict, rules: list) -> bool:
    return all(rule in passport for rule in rules)

def check_rule(rule_key: str, value: str, rules: dict = rules):
    if not rule_key in rules:
        print(f"{rule_key} not in rules.")
        return False
    rule = rules[rule_key]
    t = False
    if rule_key in ('byr', 'iyr', 'eyr'):
        if is_int(value) and rule['low'] <= int(value) <= rule['high']:
            t = True
        else:
            print(f"{value} not in range {rule['low']} {rule['high']}")
    elif rule_key == 'hgt':
        m, h = value[-2:], value[:-2]
        if m in ('cm', 'in'):
            if is_int(h) and rule[m]['low'] <= int(h) <= rule[m]['high']:
                t = True
            else:
                print(f"{value} not in range {rule[m]['low']} {rule[m]['high']}")
        else:
            print(f"{value} not valid height measurement.")
    elif rule_key == 'hcl':
        if bool(re.match(rule['re'], value)):
            t = True
        else:
            print(f"{value} is not a valid hair color.")
    elif rule_key == 'ecl':
        if value in rule['cl']:
            t = True
        else:
            print(f"{value} not a valid eye color.")
    elif rule_key == 'pid':
        if bool(re.match(rule['re'], value)):
            t = True
        else:
            print(f"{value} not valid passport id.")
    elif rule_key == 'cid':
        t = True
    return t

def passport_validation(passport: dict, rules: dict) -> bool:
    x = naive_passport_validation(passport, naive_rules)
    y = all(check_rule(key, value, rules) for key, value in passport.items())
    print(x, y)
    return x and y

if __name__ == '__main__':
    passports = parse_passports(raw_passports)
    print('A1:', sum(naive_passport_validation(passport, naive_rules)
                     for passport in passports))

    print('A2:', sum(passport_validation(passport, rules)
                     for passport in passports))
