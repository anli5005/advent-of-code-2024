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
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

result = 0

def mix(a, b):
    return a ^ b

def prune(s):
    return s % 16777216

def iterate(s):
    s = prune(mix(s, s * 64))
    s = prune(mix(s, s // 32))
    s = prune(mix(s, s * 2048))
    return s

for line in lines:
    s = int(line)
    for i in range(2000):
        s = iterate(s)
    result += s

print(result)
