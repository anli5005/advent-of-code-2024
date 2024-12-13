import sys
import re
from collections import *
from itertools import *
from heapq import *

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
claws = [lines.split("\n") for lines in inp.split("\n\n")]
r = r".*X[+=](\d+), Y[+=](\d+)"

result = 0

def get_match(line):
    match = re.match(r, line)
    return int(match[1]), int(match[2])

for claw in claws:
    a = get_match(claw[0])
    b = get_match(claw[1])
    prize = get_match(claw[2])

    q = [(0, 0, 0)]
    visited = set()
    while q:
        current = heappop(q)
        if (current[1], current[2]) in visited:
            continue
        visited.add((current[1], current[2]))
        if current[1] == prize[0] and current[2] == prize[1]:
            print(f"Machine {prize} -> {current[0]}")
            result += current[0]
            break
        elif current[1] <= prize[0] and current[2] <= prize[1]:
            heappush(q, (current[0] + 3, current[1] + a[0], current[2] + a[1]))
            heappush(q, (current[0] + 1, current[1] + b[0], current[2] + b[1]))

print(result)
