"""
Directions
-----------
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Example 1:
-----------
Input: [2,2,1]
Output: 1

Example 2:
-----------
Input: [4,1,2,1,2]
Output: 4
"""


from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List
        :rtype: Integer
        """
        arr = Counter(nums)
        return arr.most_common()[::-1][0][0]


if __name__ == "__main__":
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
