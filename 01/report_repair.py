from itertools import permutations
from math import prod

def report_prod(list_: list, sum_: int, nums: int):
    """
        Find the product where 'n' number of numbers from list 'list_' sum to 'sum_',
        print sum and product of the first match.
    """
    for numbers in permutations(list_, nums):
        if sum(numbers) == sum_:
            print(' + '.join(str(i) for i in numbers), f"= {sum_}")
            print(' * '.join(str(i) for i in numbers), f"= {prod(numbers)}")
            break

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        expenses = [int(line) for line in f.readlines()]
    
    print("Q1: Find the two entries that sum to 2020; what do you get if you",
          "multiply them together?")
    report_prod(list_=expenses, sum_=2020, nums=2)
    
    print("Q2: In your expense report, what is the product of the three",
          "entries that sum to 2020?")
    report_prod(list_=expenses, sum_=2020, nums=3)
