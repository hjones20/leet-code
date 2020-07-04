"""
Directions:
-----------
Given an array of integers, return indices of the two numbers such that they add up to a specific
target. You may assume that each input would have exactly one solution, and you may not use the
same element twice.

Example:
--------
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums: list, target: int) -> list:
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        # if remainder is already in seen dict, return value (index) in dict corresponding to
        # remainder value (key) plus the index corresponding to the current value, v (as a list)
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
        print(seen)
    return []


print(two_sum([3, 2, 4], 7))

