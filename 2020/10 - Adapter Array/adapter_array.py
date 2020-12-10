from functools import lru_cache

with open('input.txt', 'r') as f:
    adapters = [int(i) for i in f.read().splitlines()]

adapters = [0] + sorted(adapters) + [max(adapters) + 3]

def part_1():
    diffs = [0, 0, 0]
    for a, b in zip(adapters[:-1], adapters[1:]):
        diff = b - a
        diffs[diff - 1] += 1
    return diffs[0] * diffs[2]

@lru_cache()
def part_2(s_pos: int = 0):
    count = 0
    end = adapters[-1]
    for n_pos in range(s_pos + 1, len(adapters)):
        if adapters[n_pos] - adapters[s_pos] <= 3:
            if end == adapters[n_pos]:
                count += 1
            count += part_2(n_pos)
        else:
            break
    return count


print('A1:', part_1())
print('A2:', part_2())
