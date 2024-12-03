import sys
import re

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

r = r"mul\((\d+),(\d+)\)"

result = 0

for line in lines:
    for match in re.findall(r, line):
        result += int(match[0]) * int(match[1])

print(result)
