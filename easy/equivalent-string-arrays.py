"""
Directions:
-----------
Given two string arrays word1 and word2, return true if the two arrays represent the same string,
and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
-----------
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""


class Solution(object):

    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: Boolean
        """
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        return word1 == word2


if __name__ == "__main__":

    print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
