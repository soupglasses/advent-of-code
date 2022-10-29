#!/usr/bin/env python3
"""
AOC Runner
"""
import argparse
import re
from pathlib import Path
from subprocess import  Popen, PIPE

parser = argparse.ArgumentParser(description="Advent of Code helper")
parser.add_argument("program", type=str, help="The program to run")
parser.add_argument("--attempt", dest="source", action="store_const",
                    const="input", default="example",
                    help="Attempt to run with the solution")

args = parser.parse_args()

path = Path(args.program)

if match := re.search(r"\d{2}", path.name):
    day = match.group(0)
else:
    raise Exception(f"Program name {path.name!r} does not conatin a 2 digit number.")

with open(path.parent / "inputs" / f"{args.source}_{day}.txt", encoding="utf-8") as f:
    process = Popen([f"{path.parent}/{path.name}"], stdin=f, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output, err = output.decode("utf-8"), err.decode("utf-8")

if exit_code != 0:
    if output:
        print(output)
    if err:
        print(err)
    raise Exception("Program exited with non-zero exitcode.")

with open(path.parent / "outputs" / f"{args.source}_{day}.txt", encoding="utf-8") as f:
    expected_output = f.read()

if output != expected_output:
    print("Output does not match expected input.")
    print("\nOutput:")
    print(output)
    print("Expected:")
    print(expected_output)
