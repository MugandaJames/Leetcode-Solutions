class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []
        path = []

        def backtrack(start):

            result.append(path[:])

            for i in range(start, len(nums)):

                # skip duplicates at same tree level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1)

                path.pop()

        backtrack(0)

        return result
