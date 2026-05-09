class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = 0          # pointer for s
        j = 0          # pointer for p
        star = -1      # last position of '*'
        match = 0      # position in s when '*' was found

        while i < len(s):

            # characters match OR '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # mismatch but previous '*' exists
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # mismatch and no '*'
            else:
                return False

        # remaining characters in p must all be '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
