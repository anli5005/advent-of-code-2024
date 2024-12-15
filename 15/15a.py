import sys
import re
from collections import *
from itertools import *
from heapq import *
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
parts = inp.split("\n\n")
lines = parts[0].split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chardirs = {"<": 1, ">": 0, "^": 2, "v": 3}
# diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

result = 0

def move(d, i, j):
    if grid[i][j] == "#":
        return False
    elif grid[i][j] == ".":
        return True
    else:
        can_move = move(d, i + d[0], j + d[1])
        if can_move:
            grid[i + d[0]][j + d[1]] = grid[i][j]
            grid[i][j] = "."
            return True
        return False

robot_pos = (0, 0)
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            robot_pos = (i, j)

for dirchar in parts[1]:
    if dirchar == "\n":
        continue
    d = dirs[chardirs[dirchar]]
    if move(d, robot_pos[0], robot_pos[1]):
        robot_pos = (robot_pos[0] + d[0], robot_pos[1] + d[1])

for i in range(m):
    for j in range(n):
        if grid[i][j] == "O":
            result += 100 * i + j

print(result)
