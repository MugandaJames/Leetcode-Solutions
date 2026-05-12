class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # clearly in right half
            if nums[mid] > nums[right]:
                left = mid + 1

            # clearly in left half
            elif nums[mid] < nums[right]:
                right = mid

            # duplicates case → cannot decide
            else:
                right -= 1

        return nums[left]
