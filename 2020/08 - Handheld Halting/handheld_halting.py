def break_at_recursion(stepper):
    def stepper_wrapper(prog: list, step: int = 0, acc: int = 0):
        steps = set()
        run = stepper(prog, step, acc)
        while len(run['prog']) > run['step']:
            if run['step'] in steps:
                run['err'] = True
                return run
            else:
                steps.add(run['step'])
            run = stepper(**run)
        run['err'] = False
        return run
    return stepper_wrapper

@break_at_recursion
def stepper(prog: list, step: int = 0, acc: int = 0):
    op, i = prog[step]
    if op == 'nop':
        return {'prog': prog, 'step': step + 1, 'acc': acc}
    elif op == 'acc':
        return {'prog': prog, 'step': step + 1, 'acc': acc + i}
    elif op == 'jmp':
        return {'prog': prog, 'step': step + i, 'acc': acc}

def part_2_deltas(prog: list) -> list:
    return [(step, 'jmp', i) if op == 'nop'
            else (step, 'nop', i)
            for step, (op, i) in enumerate(prog)
            if op in ('jmp', 'nop')]

def terminating_delta(prog: list, prog_deltas: list):
    for step, op, i in prog_deltas:
        prog_with_delta = list(prog)
        prog_with_delta[step] = (op, i)
        ret_vals = stepper(prog_with_delta)
        if ret_vals['err'] is False:
            return ret_vals


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        prog = [(line.split()[0], int(line.split()[1]))
                for line in f.read().splitlines()]

    print('A1:', stepper(prog)['acc'])
    prog_deltas = part_2_deltas(prog)
    print('A2:', terminating_delta(prog, prog_deltas)['acc'])
