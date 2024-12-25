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
schematics = inp.split("\n\n")

m = 7
n = 5

keys = []
locks = []

for schematic in schematics:
    lines = schematic.split("\n")
    grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
    counts = []
    for i in range(n):
        c = 0
        for j in range(m):
            if grid[j][i] == "#":
                c += 1
        counts.append(c)
    if lines[0] == ".....":
        keys.append(counts)
    else:
        locks.append(counts)

def fits(key, lock):
    for i in range(n):
        if key[i] + lock[i] > m:
            return False
    return True

result = 0
for key in keys:
    for lock in locks:
        if fits(key, lock):
            result += 1

print(result)
