class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s) - 1
        length = 0

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # count last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
