import sys
import re
from collections import *
from itertools import *
from heapq import *
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

result = 1111111

start_pos = None
end_pos = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == "S":
            start_pos = (i, j)
        elif grid[i][j] == "E":
            end_pos = (i, j)

q = [(0, (start_pos, 0))]
visited = set()
while q:
    current = heappop(q)
    if current[1] in visited:
        continue
    visited.add(current[1])
    print(current)
    if grid[current[1][0][0]][current[1][0][1]] == "#":
        continue
    if current[1][0] == end_pos:
        result = current[0]
        break
    d = dirs[current[1][1]]
    heappush(q, (current[0] + 1, ((current[1][0][0] + d[0], current[1][0][1] + d[1]), current[1][1])))
    for delta in [-1, 1]:
        new_index = (current[1][1] + delta + len(dirs)) % len(dirs)
        heappush(q, (current[0] + 1000, (current[1][0], new_index)))

print(result)
