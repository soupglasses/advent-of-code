from itertools import permutations
from math import prod

sum_ = 2020

def report_prod(list_: list, sum_: int, nums: int):
    """
        Find the product where 'n' number of numbers from list 'list_' sum to 'sum_',
        pretty print sum and product of the first match.
    """
    for numbers in permutations(list_, nums):
        if sum(numbers) == sum_:
            print(' + '.join(str(i) for i in numbers), f"= {sum_}")
            print(' * '.join(str(i) for i in numbers), f"= {prod(numbers)}")
            break

if __name__ == '__main__':
    """ 
        Q1: Find the two entries that sum to 2020; what do you get if you
            multiply them together?
        Q2: In your expense report, what is the product of the three entries
            that sum to 2020?
    """
    with open('input.txt', 'r') as f:
        expenses = [int(line) for line in f.readlines()]
    
    print('Q1:')
    report_prod(list_=expenses, sum_=sum_, nums=2)
    print('Q2:')
    report_prod(list_=expenses, sum_=sum_, nums=3)
