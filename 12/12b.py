import sys
import re
from collections import *
from itertools import *

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

region = [[-1 for j in range(n)] for i in range(m)]
next_region = 0
grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

result = 0

def search(start_i, start_j, current_region):
    ch = grid[start_i][start_j]
    visited = set()
    q = deque()
    q.appendleft((start_i, start_j))
    area = 0
    sides = 0
    while q:
        i, j = q.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        region[i][j] = current_region
        area += 1
        for di, dj in dirs:
            if grid[i + di][j + dj] == ch:
                q.appendleft((i + di, j + dj))
        for di, dj in diag:
            if grid[i + di][j + dj] != ch and grid[i + di][j] == ch and grid[i][j + dj] == ch:
                sides += 1
            elif grid[i + di][j] != ch and grid[i][j + dj] != ch:
                sides += 1
    return sides, area


for i in range(m):
    for j in range(n):
        if region[i][j] == -1:
            sides, area = search(i, j, next_region)
            print(f"Region of {grid[i][j]} at ({i}, {j}) -> {next_region} ({sides} sides, {area} area)")
            result += sides * area
            next_region += 1

print(result)
