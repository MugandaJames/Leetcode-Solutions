class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        farthest = 0

        for i in range(len(nums)):

            # if current position is unreachable
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            # early exit if we already can reach end
            if farthest >= len(nums) - 1:
                return True

        return True
