import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import functools
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
parts = inp.split("\n\n")

wires = {}

for line in parts[0].split("\n"):
    p = line.split(": ")
    wires[p[0]] = p[1] == "1"

print(wires)
unprocessed = list(parts[1].split("\n"))
new_unprocessed = list()
last_len = 0

while last_len != len(unprocessed):
    print(f"Processing {len(unprocessed)} statements with {len(wires)} wires")
    for line in unprocessed:
        p = line.split(" ")
        if p[0] not in wires or p[2] not in wires:
            new_unprocessed.append(line)
            continue
        a = wires[p[0]]
        b = wires[p[2]]
        op = p[1]
        if op == "AND":
            c = a and b
        elif op == "OR":
            c = a or b
        elif op == "XOR":
            c = a != b
        else:
            print("Unrecognized op!")
        wires[p[4]] = c
    unprocessed = new_unprocessed
    new_unprocessed = list()

result = ""
keys = list(sorted(filter(lambda k: k.startswith("z"), wires.keys())))[::-1]
for k in keys:
    result += "1" if wires[k] else "0"

print(result)
print(int(result, 2))
