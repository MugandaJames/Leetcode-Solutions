class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):

            total = 0

            for root in range(1, i + 1):

                left = dp[root - 1]
                right = dp[i - root]

                total += left * right

            dp[i] = total

        return dp[n]
