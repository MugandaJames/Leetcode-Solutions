# The read4 API is already defined for you.
# def read4(buf4):
#     return number of characters read

class Solution(object):

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """

        total = 0
        temp = [""] * 4

        while total < n:

            count = read4(temp)

            if count == 0:
                break  # EOF

            for i in range(count):

                if total == n:
                    break

                buf[total] = temp[i]
                total += 1

        return total
