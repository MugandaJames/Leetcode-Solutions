class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        result = []

        # handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        n, d = abs(numerator), abs(denominator)

        # integer part
        result.append(str(n // d))
        remainder = n % d

        if remainder == 0:
            return "".join(result)

        result.append(".")
        seen = {}

        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // d))
            remainder %= d

        return "".join(result)
