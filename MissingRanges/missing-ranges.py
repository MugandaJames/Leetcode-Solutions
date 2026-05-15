from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format(a, b):
            if a == b:
                return str(a)
            return f"{a}->{b}"

        res = []
        prev = lower - 1

        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if curr - prev >= 2:
                res.append(format(prev + 1, curr - 1))

            prev = curr

        return res
