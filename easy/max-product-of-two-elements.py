"""
Directions:
------------
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:
----------
Input: nums = [3,4,5,2]
Output: 12

Explanation:
------------
If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is,
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""

# ------------------------------
# Complicated, slow solution:
# ------------------------------


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List
        :rtype: Integer
        """
        products = []

        for index, value in enumerate(nums):
            for i, v in enumerate(nums):
                if index != i:
                    products.append((value - 1) * (v - 1))

        return max(products)


if __name__ == "__main__":

    print(Solution().maxProduct([3, 4, 5, 2]))


# ------------------------------
# Simple, fast solution:
# ------------------------------

class Solution(object):

    def maxProduct(self, nums):
        nums.sort(reverse=True)

        return (nums[0]-1)*(nums[1]-1)
