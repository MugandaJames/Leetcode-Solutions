class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        numbers = [str(i) for i in range(1, n + 1)]

        # factorial of (n-1)
        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1  # convert to 0-based indexing

        result = []

        while numbers:

            index = k // fact
            result.append(numbers[index])

            numbers.pop(index)

            if not numbers:
                break

            k %= fact
            fact //= len(numbers)

        return "".join(result)
