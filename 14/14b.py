import sys
import re
from collections import *
from itertools import *
from heapq import *
import math
import time

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = 101
n = 103
r = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
robots = [[int(x) for x in [re.match(r, line)[1], re.match(r, line)[2], re.match(r, line)[3], re.match(r, line)[4]]] for line in lines]

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

def search(start_i, start_j, grid):
    ch = grid[start_i][start_j]
    visited = set()
    q = deque()
    q.appendleft((start_i, start_j))
    area = 0
    while q:
        i, j = q.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        area += 1
        for di, dj in dirs:
            try:
                if grid[i + di][j + dj] == "#":
                    q.appendleft((i + di, j + dj))
            except:
                pass
    return area

i = 0
while True:
    grid = [["." for x in range(m)] for y in range(n)]
    for robot in robots:
        robot[0] = (robot[0] + robot[2] + m) % m
        robot[1] = (robot[1] + robot[3] + n) % n
        grid[robot[1]][robot[0]] = "#"
    max_bunch = max(search(robot[1], robot[0], grid) for robot in robots)
    i += 1
    print(f"Second {i} -> {max_bunch}")
    for l in grid:
        print("".join(l))
    if max_bunch >= 20:
        time.sleep(2)