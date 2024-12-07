import sys
import re
from collections import *

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")

result = 0

def get_tries(nums):
    if len(nums) == 1:
        return set([nums[0]])
    subresult = get_tries(nums[1:])
    result = set()
    result.update(nums[0] * x for x in subresult)
    result.update(nums[0] + x for x in subresult)
    result.update(int(str(x) + str(nums[0])) for x in subresult)
    return result

for line in lines:
    parts = line.split(": ")
    subparts = [int(x) for x in parts[1].split(" ")]
    r = get_tries(subparts[::-1])
    print(int(parts[0]) in r)
    if int(parts[0]) in r:
        result += int(parts[0])

print(result)
