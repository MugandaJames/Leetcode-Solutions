class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        # Check all 32 bits
        for i in range(32):

            bit_sum = 0

            for num in nums:
                bit_sum += (num >> i) & 1

            # Remaining bit after removing triples
            if bit_sum % 3:

                # Handle negative numbers
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)

        return result
