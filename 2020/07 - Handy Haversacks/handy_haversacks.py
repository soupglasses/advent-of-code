import re

RE_BAG_RULES = re.compile(r'(\d+) (\w+ \w+)')


def parse(raw_rules: str) -> dict[str, list]:
    """Returns a dictionary with keys of the bag's color and a list with
    tuples containing the rules that the bag needs to follow.
    """
    rules = {}
    raw_rules_split = [rule.split(' contain ')
                       for rule in raw_rules.splitlines()]
    for left, right in raw_rules_split:
        bag = left.replace(' bags', '')
        bag_rules = RE_BAG_RULES.findall(right)
        rules[bag] = [(int(count), color) for count, color in bag_rules]
    return rules

def bags_containing_bag(bag: str, rules: dict[str, list]) -> int:
    """Returns the bags that have bag in their rules."""
    return {r_bag
            for r_bag, r_rule in rules.items()
            for _, r_color in r_rule
            if bag in r_color}

def fits_in_bags(bag: str, rules: dict[str, list]) -> set:
    """Returns a set of all `bag` colors that bag can fit into
    following `rules`.
    """
    bags = bags_containing_bag(bag, rules)
    all_bags = set()
    for bag_color in bags:
        all_bags |= fits_in_bags(bag_color, rules)
    return bags | all_bags

def required_bags(bag: str, count: int, rules: dict[str, list]) -> int:
    """Returns the total amount of bags required to fit `bag` into bag,
    following the given `rules`.

    Note: Return includes the top `bag`(s), subtract the return value
    by `count` to get total bags needed inside of the parent bag.
    """
    return count + sum(required_bags(bcolor, bcount, rules) * count
                       for bcount, bcolor in rules[bag])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rules = parse(f.read())

    print('Q1:', 'How many bag colors can eventually contain at least one',
          'shiny gold bag?')
    print('A1:', len(fits_in_bags('shiny gold', rules)))

    print('Q2:', 'How many individual bags are required inside your single',
          'shiny gold bag?')
    print('A2:', required_bags('shiny gold', 1, rules) - 1)