"""
Directions
-----------
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of
nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
-----------
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]

Explanation:
-------------
- For number 4 in the first array, you cannot find the next greater number for it in the second
  array, so output -1.
- For number 1 in the first array, the next greater number for it in the second array is 3.
- For number 2 in the first array, there is no next greater number for it in the second array,
  so output -1.
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List
        :type nums2: List
        :rtype: List
        """
        result = []
        for num in nums1:
            index = nums2.index(num) + 1

            if index == len(nums2):
                result.append(-1)
                continue

            while index < len(nums2):
                if nums2[index] > num:
                    result.append(nums2[index])
                    break

                elif index >= len(nums2) - 1:
                    result.append(-1)

                index += 1

        return result


if __name__ == "__main__":

    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))

