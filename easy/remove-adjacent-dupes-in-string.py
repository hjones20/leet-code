"""
Directions:
------------
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and
equal letters, and removing them. We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed the
answer is unique.

Example 1:
-----------
Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is
the only possible move.  The result of this move is that the string is "aaca", of which only "aa"
is possible, so the final string is "ca".
"""


class Solution(object):

    def removeDuplicates(self, S):
        """
        :type S: String
        :rtype: String
        """
        input_string = list(S)
        result_list = list(input_string[0])

        for char in input_string[1:]:
            if result_list and char == result_list[-1]:
                result_list.pop()
            else:
                result_list.append(char)

        return "".join(result_list)


if __name__ == "__main__":

    test_case = "abbaca"
    print(Solution().removeDuplicates(test_case))


