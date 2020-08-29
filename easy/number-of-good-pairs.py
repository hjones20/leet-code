"""
Directions
-----------
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:
-----------
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""


class Solution(object):

    def numIdenticalPairs(self, nums):
        """
        :type nums: List of integers
        :rtype: Integer
        """

        good_pairs = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] == nums[x]:
                    good_pairs += 1

        return good_pairs


if __name__ == "__main__":

    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))




