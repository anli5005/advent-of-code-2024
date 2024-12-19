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
def can_do(pattern: str):
    if pattern == "":
        return True
    for candidate in available:
        if pattern.startswith(candidate):
            if can_do(pattern[len(candidate):]):
                return True
    return False

for line in lines:
    if can_do(line):
        result += 1

print(result)
