"""
Directions:
------------
Given an array of integers arr, write a function that returns true if and only if the number of
occurrences of each value in the array is unique.

Example 1:
-----------
Input: arr = [1,2,2,1,1,3]
Output: true

Explanation:
-------------
The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of
occurrences.
"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List
        :rtype: Boolean
        """
        results = {}

        for num in arr:
            if num not in results:
                results[num] = 1
            else:
                results[num] += 1

        if len(results.values()) == len(set(results.values())):
            return True
        else:
            return False


if __name__ == "__main__":

    print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
