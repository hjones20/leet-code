"""
Directions:
-----------
Given an integer number n, return the difference between the product of its digits and the sum of
its digits.

Example:
---------
Input: n = 234
Output: 15

Explanation:
-------------
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""


class Solution(object):

    def subtractProductAndSum(self, n):
        """
        :type n: Integer
        :rtype: Integer
        """
        total_sum = 0
        total_product = 1

        for digit in str(n):
            total_sum += int(digit)
            total_product *= int(digit)

        return total_product - total_sum


if __name__ == "__main__":

    print(Solution().subtractProductAndSum(234))
