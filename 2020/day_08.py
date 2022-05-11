import sys
from typing import Optional

def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = [(line.split()[0], int(line.split()[1]))
            for line in raw.splitlines()]
    return data


def stop_at_recursion(stepper):
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


@stop_at_recursion
def stepper(prog: list, step: int, acc: int):
    op, i = prog[step]
    if op == 'nop':
        return {'prog': prog, 'step': step + 1, 'acc': acc}
    elif op == 'acc':
        return {'prog': prog, 'step': step + 1, 'acc': acc + i}
    elif op == 'jmp':
        return {'prog': prog, 'step': step + i, 'acc': acc}


def generate_deltas(prog: list) -> list:
    return [(step, 'jmp', i) if op == 'nop'
            else (step, 'nop', i)
            for step, (op, i) in enumerate(prog)
            if op in ('jmp', 'nop')]


def part_2(prog: list, prog_deltas: list):
    prog = list(prog)
    for step, op, i in prog_deltas:
        old_delta = prog[step]
        prog[step] = (op, i)
        ret_vals = stepper(prog)
        prog[step] = old_delta
        if ret_vals['err'] is False:
            return ret_vals


if __name__ == '__main__':
    program = parse_data("inputs/example_08.txt")

    print('A1:', stepper(program)['acc'])

    all_deltas = generate_deltas(program)
    print('A2:', part_2(program, all_deltas)['acc'])
