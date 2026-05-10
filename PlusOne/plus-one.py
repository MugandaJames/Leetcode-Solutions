class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        # move from right to left
        for i in range(n - 1, -1, -1):

            # no carry needed
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # carry
            digits[i] = 0

        # all digits were 9
        return [1] + digits
