class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()

        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, char in enumerate(s):

            # digit
            if char.isdigit():
                seen_digit = True

            # sign
            elif char in ['+', '-']:

                # sign only allowed:
                # at start OR after exponent
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            # decimal point
            elif char == '.':

                # dot can't appear after exponent
                # or appear twice
                if seen_dot or seen_exponent:
                    return False

                seen_dot = True

            # exponent
            elif char in ['e', 'E']:

                # exponent must appear once
                # and must follow a number
                if seen_exponent or not seen_digit:
                    return False

                seen_exponent = True

                # must have digits after exponent
                seen_digit = False

            else:
                return False

        return seen_digit
