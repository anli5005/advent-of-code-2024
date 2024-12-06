import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")
a = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))

i = 0
j = 0
for ai in range(len(lines)):
    for aj in range(len(lines[0])):
        if a[ai][aj] == "^":
            i = ai
            j = aj

print(i, j)
result = 0
current = (-1, 0)
while a[i][j] != "!":
    if a[i][j] != "X":
        a[i][j] = "X"
        result += 1
    if a[i + current[0]][j + current[1]] == "#":
        current = (current[1], -current[0])
    else:
        i += current[0]
        j += current[1]
    print(i, j, current)

print(result)
