"""
Directions:
-----------
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
-----------
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
-----------
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Constraints:
-------------
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


class Solution(object):

    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_list = []
        cumulative = 0

        for i in nums:
            cumulative += i
            output_list.append(cumulative)

        return output_list


if __name__ == "__main__":

    test_case = [1, 1, 1, 1]
    print(Solution().runningSum(test_case))
