import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")
a = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))

si = 0
sj = 0
for ai in range(len(lines)):
    for aj in range(len(lines[0])):
        if a[ai][aj] == "^":
            si = ai
            sj = aj

result = 0
for oi in range(len(lines)):
    print(f"{oi}/{len(lines)}")
    for oj in range(len(lines)):
        i = si
        j = sj
        if a[oi][oj] != ".":
            continue
        a[oi][oj] = "#"
        steps = 0
        current = (-1, 0)
        while a[i][j] != "!":
            steps += 1
            if a[i + current[0]][j + current[1]] == "#":
                current = (current[1], -current[0])
            else:
                i += current[0]
                j += current[1]
            if steps >= 20000:
                result += 1
                break
        a[oi][oj] = "."

print(result)
