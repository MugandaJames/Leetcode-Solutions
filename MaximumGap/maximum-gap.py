class Solution(object):
    def maximumGap(self, nums):
        if not nums or len(nums) < 2:
            return 0

        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        n = len(nums)

        # bucket size (minimum 1 to avoid division by zero)
        size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // size + 1

        buckets = [[None, None] for _ in range(bucket_count)]
        # each bucket = [min, max]

        for num in nums:
            idx = (num - mn) // size

            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = None

        for bmin, bmax in buckets:
            if bmin is None:
                continue
            if prev_max is not None:
                max_gap = max(max_gap, bmin - prev_max)
            prev_max = bmax

        return max_gap
