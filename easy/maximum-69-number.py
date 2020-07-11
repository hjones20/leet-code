"""
Directions:
------------
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
-----------
Input: num = 9669
Output: 9969

Explanation:
-------------
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 3:
------------
Input: num = 9999
Output: 9999

Explanation:
-------------
It is better not to apply any change.
"""


class Solution(object):

    def maximum69Number(self, num):
        """
        :type num: Integer
        :rtype: Integer
        """
        num_list = [int(x) for x in str(num)]

        for index, integer in enumerate(num_list):
            if integer != 9:
                num_list[index] = 9
                break

        convert_to_str = [str(x) for x in num_list]

        return int("".join(convert_to_str))


if __name__ == "__main__":

    print(Solution().maximum69Number(9669))


# Slightly slower, but simpler solution:
class Solution(object):

    def maximum69Number(self, num):
        """
        :type num: Integer
        :rtype: Integer
        """
        original_str = str(num)
        counter = -1  # start here to account for zero-indexing

        for char in original_str:
            counter += 1
            if char != '9':
                break

        result = int(original_str[:counter] + '9' + original_str[counter+1:])

        return result
