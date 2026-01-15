class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        num = 0
        n = len(s)
        sign = 1

        #handle space
        while i < n and s[i] == ' ':
            i += 1

        #handle sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # converting to digits

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # checking for overflow before adding 

            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            num = num * 10 + digit
            i += 1
        
        return sign * num

        
