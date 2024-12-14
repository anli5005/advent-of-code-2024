import sys
import re
from collections import *
from itertools import *
from heapq import *
import math
import time

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = 101
n = 103
r = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
robots = [[int(x) for x in [re.match(r, line)[1], re.match(r, line)[2], re.match(r, line)[3], re.match(r, line)[4]]] for line in lines]

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

for i in range(100):
    for robot in robots:
        robot[0] = (robot[0] + robot[2] + m) % m
        robot[1] = (robot[1] + robot[3] + n) % n

tr, tl, bl, br = 0, 0, 0, 0
for robot in robots:
    if robot[0] < 50 and robot[1] < 51:
        tr += 1
    elif robot[0] < 50 and robot[1] > 51:
        tl += 1
    elif robot[0] > 50 and robot[1] < 51:
        bl += 1
    elif robot[0] > 50 and robot[1] > 51:
        br += 1

result = tr * tl * bl * br

print(result)
