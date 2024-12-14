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
global_min_grid = None
min_safety = float("inf")
min_second = 0
for i in range(100000):
    grid = [["." for x in range(m)] for y in range(n)]
    for robot in robots:
        robot[0] = (robot[0] + robot[2] + m) % m
        robot[1] = (robot[1] + robot[3] + n) % n
        grid[robot[1]][robot[0]] = "#"
    max_bunch = max(search(robot[1], robot[0], grid) for robot in robots)
    i += 1
    tr, tl, bl, br = 0, 0, 0, 0
    for robot in robots:
        if robot[0] < 50 and robot[1] < 51:
            tr += 1
        elif robot[0] < 50 and robot[1] > 51:
            tl += 1
        elif robot[0] > 50 and robot[1] < 51:
            bl += 1
        elif robot[0] > 50 and robot[1] > 51:
            br += 1
    safety_score = tr * tl * bl * br
    if i % 10000 == 0:
        print(f"Second {i}")
    if safety_score < min_safety:
        min_safety = safety_score
        min_second = i
        global_min_grid = grid
    #if max_bunch >= 20:
    #    time.sleep(2)

print(f"Second {min_second} -> {min_safety}")
for l in global_min_grid:
    print("".join(l))