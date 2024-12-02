import sys
import re

def count(it):
    return sum(1 for _ in it)

lines = sys.stdin.read().split("\n")



result = 0

def is_safe(nums):
    is_safe = True
    status = None
    last = nums[0]
    for i in range(1, len(nums)):
        diff = abs(nums[i] - last)
        if diff < 1 or diff > 3:
            is_safe = False
        if status is None:
            if nums[i] < last:
                status = False
            else:
                status = True
        elif status:
            if nums[i] < last:
                is_safe = False
        else:
            if nums[i] > last:
                is_safe = False
        last = nums[i]
    return is_safe

for line in lines:
    nums = [int(x) for x in line.split(" ")]
    safe = is_safe(nums)
    for i in range(len(nums)):
        safe = safe or is_safe(nums[:i] + nums[(i+1):])
    if safe:
        result += 1


print(result)
