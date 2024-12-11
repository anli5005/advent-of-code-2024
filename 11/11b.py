import sys
import re
from collections import *
from itertools import *

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
stones = [int(p) for p in inp.split(" ")]
n = len(stones)
stones = Counter(stones)

for i in range(75):
    new_stones = Counter()
    print(f"Stage {i}: {stones.total()} stones")
    for stone, amount in stones.items():
        s = str(stone)
        l = len(s)
        if stone == 0:
            new_stones[1] += amount
        elif l % 2 == 0:
            new_stones[int(s[:(l // 2)])] += amount
            new_stones[int(s[(l // 2):])] += amount
        else:
            new_stones[stone * 2024] += amount
    stones = new_stones

print(stones.total())
