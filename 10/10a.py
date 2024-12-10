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

result = 0

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(m):
    for j in range(n):
        if a[i][j] == "0":
            states = deque()
            states.append((i, j))
            visited = set()
            while states:
                current = states.popleft()
                if current in visited:
                    continue
                visited.add(current)
                if a[current[0]][current[1]] == "9":
                    result += 1
                elif a[current[0]][current[1]] != "!":
                    for dd in d:
                        if a[current[0] + dd[0]][current[1] + dd[1]] == str(int(a[current[0]][current[1]]) + 1):
                            states.append((current[0] + dd[0], current[1] + dd[1]))


print(result)
