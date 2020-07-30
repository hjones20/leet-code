"""
Directions
-----------
We are given two sentences A and B.  (A sentence is a string of space separated words. Each word
consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the
other sentence.

Return a list of all uncommon words. You may return the list in any order.
"""


from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: String
        :type B: String
        :rtype: List
        """
        uncommon = []

        string_a = a.split(" ")
        string_b = b.split(" ")
        counter_a = Counter(string_a)
        counter_b = Counter(string_b)

        set_difference = list(set(string_a).symmetric_difference(set(string_b)))

        for key, value in counter_a.items():
            if key in set_difference and value == 1:
                uncommon.append(key)

        for key, value in counter_b.items():
            if key in set_difference and value == 1:
                uncommon.append(key)

        return uncommon

# Slower but cleaner
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: String
        :type B: String
        :rtype: List
        """
        string_a = A.split(" ")
        string_b = B.split(" ")

        set_difference = (set(string_a).symmetric_difference(set(string_b)))
        set_dict = dict.fromkeys(set_difference, 0)

        for word in (string_a + string_b):
            if word in set_dict:
                set_dict[word] += 1

        return [key for key, value in set_dict.items() if value == 1]


if __name__ == "__main__":

    print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))
