import sys
import re
from collections import Counter

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

left = []
right = []
for l in lines:
    p = l.split("   ")
    left.append(int(p[0]))
    right.append(int(p[1]))

right = Counter(right)

result = 0
for l in left:
    result += l * right[l]


print(result)
