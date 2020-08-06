"""
Directions
-----------
A sequence of numbers is called arithmetic if it consists of at least three elements and if the
difference between any two consecutive elements is the same.

Example:
-----------
A = [1, 2, 3, 4]
Return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List
        :rtype: Integer
        """
        diff = [A[i] - A[i-1] for i in range(1, len(A))]

        sequence_counter = 0
        total_sequence_count = 0

        for i in range(1, len(diff)):
            if diff[i] == diff[i-1]:
                sequence_counter += 1
                total_sequence_count += sequence_counter
            else:
                sequence_counter = 0

        return total_sequence_count


if __name__ == "__main__":

    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))

