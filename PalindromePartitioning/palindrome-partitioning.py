class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []
        path = []

        def is_palindrome(st):

            return st == st[::-1]

        def dfs(start):

            if start == len(s):
                res.append(list(path))
                return

            for end in range(start, len(s)):

                substring = s[start:end+1]

                if is_palindrome(substring):

                    path.append(substring)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res
