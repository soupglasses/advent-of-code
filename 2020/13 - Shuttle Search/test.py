def recursive(busses: list, time: int):
    offset = 0
    for bus, jmp in busses:
        valid = ((time+offset)/bus).is_integer()
        if valid:
            offset += jmp + 1
        else:
            return False
    return True

busses = [[17, 1], [13, 0], [19, 0]]
for i in range(100_000):
    recursive(busses, 3417)
