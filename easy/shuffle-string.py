"""
Directions:
-----------
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in
the shuffled string. Return the shuffled string.

Example:
---------
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""


class Solution(object):

    def restoreString(self, s, indices):
        """
        :type s: String
        :type indices: List of integers
        :rtype: String
        """
        shuffled_string = ''
        mapping = dict(zip(indices, s))

        for key, value in sorted(mapping.items()):
            shuffled_string += value

        return shuffled_string


if __name__ == "__main__":

    print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))