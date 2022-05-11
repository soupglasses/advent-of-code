import sys
from typing import Optional

def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = raw.split('\n\n')
    return data



def count_any(groups: list[str]) -> int:
    return sum(
        len(set(''.join(group.split())))
        for group in groups
    )

def count_all(groups: list[str]) -> int:
    return sum(
        len(set.intersection(*map(set, group.splitlines())))
        for group in groups
    )


if __name__ == '__main__':
    forms = parse_data("inputs/example_06.txt")

    print('Q1:', 'For each group, count the number of questions to which',
          'anyone answered "yes". What is the sum of those counts?')
    print('A1:', count_any(forms))

    print('Q2:', 'For each group, count the number of questions to which',
          'everyone answered "yes". What is the sum of those counts?')
    print('A2:', count_all(forms))
