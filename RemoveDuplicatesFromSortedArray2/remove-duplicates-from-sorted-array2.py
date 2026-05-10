class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0  # write pointer

        for j in range(len(nums)):

            # first 2 elements always allowed
            if i < 2 or nums[j] != nums[i - 2]:

                nums[i] = nums[j]
                i += 1

        return i
