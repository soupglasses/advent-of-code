import sys
from typing import Optional

from sympy.ntheory.modular import crt


def parse_data(path: Optional[str]):
    if not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        if path:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        else:
            sys.exit("No stdin data was recived.")

    data = raw.splitlines()
    return data



with open('input.txt', 'r') as f:
    bus_ids = f.read().replace('x','0').split('\n')
    timestamp = int(bus_ids[0])
    busses = list(map(int, bus_ids[1].split(',')))

def parse_raw():
    departure_time, ids = parse_data("inputs/example_13.txt")
    moduli = []
    residues = []
    for residue, modulus in enumerate(ids.split(",")):
        if modulus.isdigit():
            moduli.append(int(modulus))
            residues.append(-residue)
    return int(departure_time), moduli, residues

departure, moduli, residues = parse_raw()

print(timestamp, busses)
print(timestamp, moduli, residues)
