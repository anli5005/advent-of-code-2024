import sys
import re

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

r = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"

result = 0
flag = True
for line in lines:
    for match in re.findall(r, line):
        print(match, flag)
        if match[0] == "do()":
            flag = True
        elif match[1] == "don't()":
            flag = False
        elif flag:
            result += int(match[3]) * int(match[4])

print(result)
