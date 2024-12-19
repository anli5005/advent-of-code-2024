import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
from functools import cache
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
inpparts = inp.split("\n\n")
available = inpparts[0].split(", ")
lines = inpparts[1].split("\n")

result = 0

@cache
def num_ways(pattern: str):
    if pattern == "":
        return 1
    ways = 0
    for candidate in available:
        if pattern.startswith(candidate):
            ways += num_ways(pattern[len(candidate):])
    return ways

print(sum(map(num_ways, lines)))
