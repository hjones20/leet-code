"""
Directions:
------------
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return
the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
----------
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

from itertools import chain


class Solution(object):

    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first_list = nums[:n]
        second_list = nums[n:]
        shuffled_list = zip(first_list, second_list)

        return list(chain(*shuffled_list))


if __name__ == "__main__":
    print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
