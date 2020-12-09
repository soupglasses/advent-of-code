from itertools import combinations


def encoding_valid(num: int, chunk: list[int]):
    return any(left + right == num
               for left, right in combinations(set(chunk), 2))

def find_bad_val(xmas: list[int], size: int):
    for i in range(0, len(xmas) - size):
        num = xmas[i + size]
        chunk = xmas[i:i + size]
        if not encoding_valid(num, chunk):
            return num

def break_encryption(xmas: list[int], bad_val: int):
    for size in range(2, len(xmas)):
        for i in range(0, len(xmas)):
            chunk = xmas[i:i + size]
            if sum(chunk) == bad_val:
                return min(chunk) + max(chunk)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        xmas = [int(i) for i in f.read().splitlines()]

    bad_val = find_bad_val(xmas, 25)
    print('A1:', bad_val)

    print('A2:', break_encryption(xmas, bad_val))
