import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import math

def count(it):
    return sum(1 for _ in it)

r = "Register (.): (\d+)"
parts = sys.stdin.read().split("\n\n")
registers = {}
for line in parts[0].split("\n"):
    match = re.match(r, line)
    registers[match[1]] = int(match[2])

instructions = parts[1].split("Program: ")[1].split(",")

i = 0
outs = []
while i + 1 < len(instructions):
    ins = int(instructions[i])
    i += 1
    operand = int(instructions[i])
    i += 1
    combo = operand
    if operand > 3 and operand < 7:
        combo = registers[(["A", "B", "C"])[operand - 4]]
    if ins == 0:
        registers["A"] = registers["A"] // (1 << combo)
    elif ins == 1:
        registers["B"] = registers["B"] ^ operand
    elif ins == 2:
        registers["B"] = combo % 8
    elif ins == 3:
        if registers["A"] != 0:
            i = operand
    elif ins == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif ins == 5:
        outs.append(combo % 8)
    elif ins == 6:
        registers["B"] = registers["A"] // (1 << combo)
    elif ins == 7:
        registers["C"] = registers["A"] // (1 << combo)

print(",".join(str(x) for x in outs))
