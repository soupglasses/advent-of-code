from itertools import combinations
from math import prod

with open('input.txt', 'r') as f:
    expenses = [int(line) for line in f.read().splitlines()]

def prod_from_sum(numbers: list, sum_: int, expr_len: int):
    for expr_terms in combinations(numbers, expr_len):
        if sum(expr_terms) == sum_:
            return prod(expr_terms)

print("Q1:", "Find the two entries that sum to 2020; what do you get if you",
      "multiply them together?")
print("A1:", prod_from_sum(expenses, sum_=2020, expr_len=2))

print("Q2:", "In your expense report, what is the product of the three",
      "entries that sum to 2020?")
print("A2:", prod_from_sum(expenses, sum_=2020, expr_len=3))
