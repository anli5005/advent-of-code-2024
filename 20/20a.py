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

@functools.cache
def search_nocheat(start_i, start_j, target_i, target_j):
    visited = set()
    q = deque()
    q.appendleft((0, start_i, start_j))
    while q:
        cost, i, j = q.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == target_i and j == target_j:
            return cost
        else:
            for d in dirs:
                at_pos = grid[i + d[0]][j + d[1]]
                if (at_pos != "#" and at_pos != "!") or (i + d[0] == target_i and j + d[1] == target_j):
                    q.appendleft((cost + 1, i + d[0], j + d[1]))

start_pos = None
end_pos = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start_pos = (i, j)
        elif grid[i][j] == "E":
            end_pos = (i, j)

nocheat_time = search_nocheat(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
result = 0
for si in range(m):
    print(f"Processing cheats starting at row {si}")
    for sj in range(n):
        for d in dirs:
            if grid[si + d[0]][sj + d[1]] in {".", "E"}:
                if si == end_pos[0] and sj == end_pos[1]:
                    cheat_time = search_nocheat(start_pos[0], start_pos[1], si, sj)
                else:
                    cheat_time = search_nocheat(start_pos[0], start_pos[1], si, sj) + 1 + search_nocheat(si + d[0], sj + d[1], end_pos[0], end_pos[1])
                if cheat_time <= nocheat_time - 100:
                    #print(f"Cheat saves {nocheat_time - cheat_time} ps")
                    result += 1

print(result)