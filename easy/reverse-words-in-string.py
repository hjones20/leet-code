"""
Directions:
------------
Given a string, you need to reverse the order of characters in each word within a sentence while
still preserving whitespace and initial word order.

Example 1:
-----------
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space
in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: String
        :rtype: String
        """
        split_str = s.split()
        reversed_str = []

        for word in split_str:
            reversed_str.append(word[::-1])

        return ' '.join(reversed_str)


if __name__ == "__main__":

    print(Solution().reverseWords("Let's take LeetCode contest"))
