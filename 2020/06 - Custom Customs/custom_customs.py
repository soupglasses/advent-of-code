from operator import and_
from functools import reduce

with open('input.txt', 'r') as f:
    forms = f.read().split('\n\n')

def part_1(forms: list) -> int:
    return sum(
        len(set(''.join(group.split())))
        for group in forms
    )

def part_2(forms: list) -> int:
    return sum(
        len(reduce(and_, map(set, group.splitlines())))
        for group in forms
    )

if __name__ == '__main__':
    print('Q1:', 'For each group, count the number of questions to which',
          'anyone answered "yes". What is the sum of those counts?')
    print('A1:', part_1(forms))

    print('Q2:', 'For each group, count the number of questions to which',
          'everyone answered "yes". What is the sum of those counts?')
    print('A2:', part_2(forms))
