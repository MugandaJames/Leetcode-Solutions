class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1

        rev = int(str(abs(x))[::-1])

        rev *= sign


        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        
