from itertools import permutations
from math import prod

with open('input.txt', 'r') as f:
    expenses = [int(line) for line in f.readlines()]

def prod_from_sum(numbers: list, sum_: int, width: int):
    for expr_terms in permutations(numbers, width):
        if sum(expr_terms) == sum_:
            return prod(expr_terms)

print("Q1:", "Find the two entries that sum to 2020; what do you get if you",
      "multiply them together?")
print("A1:", prod_from_sum(expenses, sum_=2020, width=2))

print("Q2:", "In your expense report, what is the product of the three",
      "entries that sum to 2020?")
print("A2:", prod_from_sum(expenses, sum_=2020, width=3))
