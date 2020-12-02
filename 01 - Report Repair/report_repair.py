from itertools import permutations
from math import prod

with open('input.txt', 'r') as f:
    expenses = [int(line) for line in f.readlines()]

def report_prod(report: list, sum_: int, permutations_: int):
    for numbers in permutations(report, permutations_):
        if sum(numbers) == sum_:
            return prod(numbers)

print('Q1:', 'Find the two entries that sum to 2020; what do you get if you',
      'multiply them together?')
print('A1:', report_prod(report=expenses, sum_=2020, permutations_=2))

print('Q2:', 'In your expense report, what is the product of the three',
      'entries that sum to 2020?')
print('A2:', report_prod(report=expenses, sum_=2020, permutations_=3))
