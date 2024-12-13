import sys
import re
from collections import *
from itertools import *
from heapq import *
import numpy as np

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
    prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)

    try:
        x = np.linalg.solve(
            np.array([a, b]).transpose(),
            np.array(prize)
        )
        
        rounded = np.round(x)
        f = abs(x - rounded)
        epsilon = 0.0001
        if f[0] < epsilon and f[1] < epsilon:
            na, nb = int(rounded[0]), int(rounded[1])
            print(na, nb, na * 3 + nb)
            result += na * 3 + nb
        else:
            print("Unsolvable")
    except np.linalg.LinAlgError:
        print("Unsolvable (non-invertible)")
        pass

print(result)
