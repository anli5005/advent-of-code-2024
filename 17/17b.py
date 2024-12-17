import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import math
from z3 import *

parts = sys.stdin.read().split("\n\n")
registers = {}
instructions = [int(x) for x in parts[1].split("Program: ")[1].split(",")]

A = BitVec("A", 128)
B = BitVecVal(0, 128)
C = BitVecVal(0, 128)
seven = BitVecVal(7, 128)
solver = Optimize()

a = A
b = B
c = C

for i in range(16):
    b = a % 8
    b = b ^ seven
    c = a >> b
    a = a >> 3
    b = b ^ c
    b = b ^ seven
    solver.add(b % 8 == instructions[i])

print(solver.minimize(A))
print(solver.check())
print(solver.model())