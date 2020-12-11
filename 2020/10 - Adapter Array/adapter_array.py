from cachetools import cached, LRUCache
from cachetools.keys import hashkey


def part_1(adapters: list[int]):
    diffs = [0, 0, 0]
    for a, b in zip(adapters[:-1], adapters[1:]):
        diff = b - a
        diffs[diff - 1] += 1
    return diffs[0] * diffs[2]

@cached(LRUCache(maxsize=256), key=lambda _, s_pos: hashkey(s_pos))
def part_2(adapters: list[int], s_pos: int):
    count = 0
    end = adapters[-1]
    s_val = adapters[s_pos]
    for n_pos in range(s_pos + 1, len(adapters)):
        n_val = adapters[n_pos]
        if n_val - s_val <= 3:
            if n_val == end:
                count += 1
            count += part_2(adapters, n_pos)
        else:
            break
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        adapters = [int(i) for i in f.read().splitlines()]

    adapters = [0] + sorted(adapters) + [max(adapters) + 3]

    print('A1:', part_1(adapters))
    print('A2:', part_2(adapters, 0))
