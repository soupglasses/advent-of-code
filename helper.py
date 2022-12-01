#!/usr/bin/env python3
"""
AOC Runner
"""
import argparse
import re
from pathlib import Path
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="Advent of Code helper")
parser.add_argument("program", type=str, help="The program to run")
parser.add_argument(
    "--attempt",
    dest="source",
    action="store_const",
    const="input",
    default="example",
    help="Attempt to run with the solution",
)

args = parser.parse_args()

program = Path(args.program)

if match := re.search(r"\d{2}", program.name):
    day = match.group(0)
else:
    raise Exception(f"Program name {program.name!r} does not conatin a 2 digit number.")

input_file = str(program.parent / "inputs" / f"{args.source}_{day}.txt")
process = Popen(
    [f"{program.parent}/{program.name}", input_file], stdout=PIPE, stderr=PIPE
)
(output, err) = process.communicate()
exit_code = process.wait()
output, err = output.decode("utf-8"), err.decode("utf-8")

if exit_code != 0:
    if output:
        print(output)
    if err:
        print(err)
    raise Exception("Program exited with non-zero exitcode.")

with open(
    program.parent / "outputs" / f"{args.source}_{day}.txt", encoding="utf-8"
) as f:
    expected_output = f.read()

if output != expected_output:
    print("Output does not match expected input.")
    print("\nOutput:")
    print(output)
    print("Expected:")
    print(expected_output)
