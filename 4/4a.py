import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

a = defaultdict((lambda: defaultdict(lambda: ".")), enumerate(defaultdict((lambda: "."), enumerate(line)) for line in lines))

result = 0

ds = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        for da, db in ds:
            d = [da, db]
            if a[i][j] == "X" and a[i + d[0]][j + d[1]] == "M" and a[i + d[0] * 2][j + d[1] * 2] == "A" and a[i + d[0] * 3][j + d[1] * 3] == "S":
                result += 1

print(result)
