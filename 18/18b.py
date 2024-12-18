import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: ".")))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def search(start_i, start_j):
    visited = set()
    q = deque()
    q.appendleft((0, start_i, start_j))
    while q:
        cost, i, j = q.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if grid[i][j] == "#" or i < 0 or i > 70 or j < 0 or j > 70:
            continue
        if i == 70 and j == 70:
            return cost
        for di, dj in dirs:
            q.appendleft((cost + 1, i + di, j + dj))

for i, line in enumerate(lines):
    parts = line.split(",")
    grid[int(parts[1])][int(parts[0])] = "#"
    if search(0, 0) is None:
        print(line)
        break
