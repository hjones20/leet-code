"""
Directions:
------------
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each
number, also in sorted non-decreasing order.

Example 1:
-----------
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List
        :rtype: List
        """
        squares = sorted([x**2 for x in A])

        return squares


if __name__ == "__main__":

    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
