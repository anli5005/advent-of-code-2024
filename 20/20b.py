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

start_pos = None
end_pos = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start_pos = (i, j)
        elif grid[i][j] == "E":
            end_pos = (i, j)

dists_from_start = {}
dists_to_end = {}

q = deque()
q.appendleft((0, start_pos[0], start_pos[1]))
while q:
    cost, i, j = q.pop()
    if (i, j) in dists_from_start:
        continue
    if grid[i][j] not in {"#", "!"}:
        dists_from_start[(i, j)] = cost
        for d in dirs:
            q.appendleft((cost + 1, i + d[0], j + d[1]))

q = deque()
q.appendleft((0, end_pos[0], end_pos[1]))
while q:
    cost, i, j = q.pop()
    if (i, j) in dists_to_end:
        continue
    if grid[i][j] not in {"#", "!"}:
        dists_to_end[(i, j)] = cost
        for d in dirs:
            q.appendleft((cost + 1, i + d[0], j + d[1]))

nocheat_time = dists_from_start[end_pos]
result = 0
for si in range(m):
    print(f"Processing cheats starting at row {si}")
    for sj in range(n):
        if grid[si][sj] in {"#", "!"}:
            continue
        for ei in range(m):
            for ej in range(n):
                if grid[ei][ej] in {"#", "!"}:
                    continue
                cheat_dist = abs(ei - si) + abs(ej - sj)
                if cheat_dist > 20:
                    continue
                cheat_time = dists_from_start[(si, sj)] + cheat_dist + dists_to_end[(ei, ej)]
                if cheat_time <= nocheat_time - 100:
                    result += 1


print(result)