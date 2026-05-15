class Solution(object):
    def convertToTitle(self, columnNumber):
        res = []

        while columnNumber > 0:
            columnNumber -= 1  # critical adjustment
            res.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return "".join(res[::-1])
