from itertools import permutations

sum_ = 2020

with open('input.txt', 'r') as f:
    expenses = [int(line) for line in f.readlines()]

for left, right in permutations(expenses, 2):
    if left + right == sum_:
        print(f"{left} + {right} = {sum_}")
        print(f"{left} * {right} = {left*right}")
        break
