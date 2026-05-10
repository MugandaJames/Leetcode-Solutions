class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        # first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                take_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                take_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[i][j] = take_s1 or take_s2

        return dp[m][n]
