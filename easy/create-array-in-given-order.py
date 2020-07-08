"""
Directions:
------------
Given two arrays of integers nums and index. Your task is to create target array under the following
rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target
array.

Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:
-----------
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""


class Solution(object):

    def createTargetArray(self, nums, index):
        """
        :type nums: List
        :type index: List
        :rtype: List
        """
        target_array = []
        array_mapping = list(zip(index, nums))

        for index, nums in array_mapping:
            target_array.insert(index, nums)

        return target_array


if __name__ == "__main__":

    print(Solution().createTargetArray([4, 2, 1, 1], [0, 0, 2, 0]))

