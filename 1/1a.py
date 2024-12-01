import sys
import re

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

left = []
right = []
for l in lines:
    p = l.split("   ")
    left.append(int(p[0]))
    right.append(int(p[1]))

left.sort()
right.sort()

def dist(l):
    return abs(int(p[1]) - int(p[0]))

result = sum(abs(l - r) for l, r in zip(left, right))


print(result)
