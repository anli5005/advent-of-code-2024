import sys
import re
from collections import *
from itertools import *

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

a = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
state = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
ch = set(inp) - set(".\n")

result = 0

for c in ch:
    positions = []
    for i in range(m):
        for j in range(n):
            if a[i][j] == c:
                positions.append((i, j))
    for pair in permutations(positions, 2):
        i = 2 * pair[0][0] - pair[1][0]
        j = 2 * pair[0][1] - pair[1][1]
        e = state[i][j]
        if e != "#" and e != "!":
            state[i][j] = "#"
            result += 1
    

print(result)
