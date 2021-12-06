from sympy.ntheory.modular import crt

with open('input.txt', 'r') as f:
    bus_ids = f.read().replace('x','0').split('\n')
    timestamp = int(bus_ids[0])
    busses = list(map(int, bus_ids[1].split(',')))

def parse_raw():
    with open("input.txt") as f:
        departure_time, ids = f.read().splitlines()
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
