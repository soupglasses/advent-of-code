from itertools import product


def set_bit(num: int, offset: int):
    return num | offset


def clear_bit(num: int, offset: int):
    return num & ~offset


def apply_mask(mask: str, num: int):
    for power, i in enumerate(reversed(mask)):
        if i == "1":
            num = set_bit(num, 2 ** power)
        elif i == "0":
            num = clear_bit(num, 2 ** power)
    return num


def apply_memory_mask(mask: str, num: int):
    floating_pos = []
    for power, i in enumerate(reversed(mask)):
        if i == "1":
            num = set_bit(num, 2 ** power)
        if i == "X":
            floating_pos.append(2 ** power)

    nums = []
    for prod_mask in product(*[[0, 1]] * len(floating_pos)):
        new_num = num
        for i, offset in zip(prod_mask, floating_pos):
            if i == 1:
                new_num = set_bit(new_num, offset)
            elif i == 0:
                new_num = clear_bit(new_num, offset)
        nums.append(new_num)

    return nums


def part1(data):
    full_mem = {}
    for mask, mem_chunk in data:
        for key, val in mem_chunk:
            full_mem[key] = apply_mask(mask, val)

    return sum(full_mem.values())


def part2(data):
    full_mem = {}
    for mask, mem_chunk in data:
        for key, val in mem_chunk:
            for mem_pos in apply_memory_mask(mask, key):
                full_mem[mem_pos] = val

    return sum(full_mem.values())


def parse_input(file_name: str):
    with open(file_name) as f:
        t = str.maketrans({"[": "", "]": "", " ": "", "m": "", "e": ""})
        lstdata = [
            match.translate(t).strip().split("\n")
            for match in f.read().split("mask = ")
        ]
        data = []
        for mask, *mem in lstdata:
            data.append((mask, list(tuple(map(int, line.split("="))) for line in mem)))
    return data


def main():
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
