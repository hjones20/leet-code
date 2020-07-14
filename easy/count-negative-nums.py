"""
Directions:
------------
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:
-----------
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

Explanation:
-------------
There are 8 negatives number in the matrix.
"""
# import numpy as np


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List of Lists
        :rtype: Integer
        """
        counter = 0
        for item in grid:
            for number in item:
                if number < 0:
                    counter += 1

        return counter


# Fastest solution
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List of Lists
        :rtype: Integer
        """
        #           [ELEMENT] [Exact same syntax as loops above] [CONDITION]
        return len([number for item in grid for number in item if number < 0])


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List of Lists
        :rtype: Integer
        """
        flat_list = [item for sublist in grid for item in sublist]
        flat_list.sort()
        counter = 0

        for item in flat_list:
            if item >= 0:
                break
            else:
                counter += 1

        return counter


# class Solution(object):
#     def countNegatives(self, grid):
#         """
#         :type grid: List of Lists
#         :rtype: Integer
#         """
#         return np.sum(np.matrix(grid) < 0)


if __name__ == "__main__":

    print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
