"""
Directions:
------------
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute
difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows:

- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
-----------
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]

Explanation:
-------------
The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""


# Inefficient solution
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List
        :return: List of Lists
        """

        results_dict = {}

        for current_num in arr:
            for comparison_num in arr:
                if current_num == comparison_num:
                    pass
                else:
                    results_dict[(current_num, comparison_num)] = abs(current_num - comparison_num)

        min_abs_value = min(results_dict.values())
        result_list = []

        for key, value in results_dict.items():
            if value == min_abs_value:
                pair = list(key)
                pair.sort()
                if pair not in result_list:
                    result_list.append(pair)
                else:
                    continue

        result_list.sort()
        return result_list


if __name__ == "__main__":

    print(Solution().minimumAbsDifference([4, 2, 1, 3]))
