import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

rulestr, updatestr = tuple(sys.stdin.read().split("\n\n"))
rulelines = rulestr.split("\n")
rules = []
for line in rulelines:
    p = line.split("|")
    rules.append((int(p[0]), int(p[1])))

updates = [[int(x) for x in line.split(",")] for line in updatestr.split("\n")]

result = 0

dep = defaultdict(lambda: [])

for a, b in rules:
    x = dep[b]
    x.append(a)
    dep[b] = x

print(dep)

for update in updates:
    correct = True
    updated = set()
    overall = set(update)
    for x in update:
        for d in dep[x]:
            if d in overall and d not in updated:
            #if d not in updated:
                correct = False
        if not correct:
            break
        updated.add(x)
    print(correct)
    if correct:
        result += update[len(update) // 2]
    # active_pages = active_pages.union(update)

print(result)
