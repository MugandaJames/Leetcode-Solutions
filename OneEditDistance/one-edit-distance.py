class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        m, n = len(s), len(t)

        # make sure s is smaller or equal
        if m > n:
            return self.isOneEditDistance(t, s)

        # length difference > 1 → impossible
        if n - m > 1:
            return False

        for i in range(m):

            if s[i] != t[i]:

                # same length → replace case
                if m == n:
                    return s[i+1:] == t[i+1:]

                # t is longer → skip one char in t
                else:
                    return s[i:] == t[i+1:]

        # no mismatch found
        return n == m + 1
