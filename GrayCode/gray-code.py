class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []

        for i in range(1 << n):

            # Gray code formula
            gray = i ^ (i >> 1)

            result.append(gray)

        return result
