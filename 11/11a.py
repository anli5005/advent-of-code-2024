import sys
import re
from collections import *
from itertools import *

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
stones = [int(p) for p in inp.split(" ")]
n = len(stones)

for i in range(25):
    new_stones = []
    for stone in stones:
        s = str(stone)
        l = len(s)
        if stone == 0:
            new_stones.append(1)
        elif l % 2 == 0:
            new_stones.append(int(s[:(l // 2)]))
            new_stones.append(int(s[(l // 2):]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))
