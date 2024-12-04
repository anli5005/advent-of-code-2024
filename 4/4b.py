import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

a = defaultdict((lambda: defaultdict(lambda: ".")), enumerate(defaultdict((lambda: "."), enumerate(line)) for line in lines))

result = 0

dss = [
    [(-1, -1), (0, 0), (1, 1)],
    [(-1, 1), (0, 0), (1, -1)],
    [(1, 1), (0, 0), (-1, -1)],
    [(1, -1), (0, 0), (-1, 1)]
]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        matches = 0
        for ds in dss:
            if a[i + ds[0][0]][j + ds[0][1]] == "M" and a[i + ds[1][0]][j + ds[1][1]] == "A" and a[i + ds[2][0]][j + ds[2][1]] == "S":
                matches += 1
        if matches >= 2:
            result += 1

print(result)
