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

for raw in updates:
    update = raw
    correct = True
    stop = False
    overall = set(update)
    while not stop:
        stop = True
        updated = set()
        for i, x in enumerate(update):
            for d in dep[x]:
                #print(f"{d}|{x}")
                if d in overall and d not in updated:
                    correct = False
                    stop = False
                    new_update = update.copy()
                    new_update[new_update.index(d)] = x
                    new_update[i] = d
                    update = new_update
                    break
            if not stop:
                break
            updated.add(x)
        #print(update)
    #print(correct)
    if not correct:
        result += update[len(update) // 2]
    # active_pages = active_pages.union(update)

print(result)
