import re

RE_BAG_RULES = re.compile(r'(\d+) (\w+ \w+)')


def parse(raw_rules: str) -> dict[str, list]:
    rules = {}
    raw_rules_split = [rule.split(' contain ')
                       for rule in raw_rules.splitlines()]
    for left, right in raw_rules_split:
        bag = left.replace(' bags', '')
        bag_rules = RE_BAG_RULES.findall(right)
        rules[bag] = [(int(count), color) for count, color in bag_rules]
    return rules

def fits_in_bags(color: str, rules: dict[str, list]) -> set:
    bags = [
        b_color
        for b_color, b_rules in rules.items()
        for _, br_color in b_rules
        if br_color and color in br_color
    ]
    all_bags = set()
    for bag_color in bags:
        all_bags |= fits_in_bags(bag_color, rules)
    return all_bags | set(bags)

def required_bags(color: str, count: int, rules: dict[str, list]) -> int:
    return count + sum(required_bags(bcolor, bcount, rules) * count
                       for bcount, bcolor in rules[color])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rules = parse(f.read())

    print('A1:', len(fits_in_bags('shiny gold', rules)))
    print('A2:', required_bags('shiny gold', 1, rules) - 1)
