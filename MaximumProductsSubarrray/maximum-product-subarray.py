class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            x = nums[i]

            temp_max = max_so_far

            max_so_far = max(x, x * max_so_far, x * min_so_far)
            min_so_far = min(x, x * temp_max, x * min_so_far)

            result = max(result, max_so_far)

        return result
