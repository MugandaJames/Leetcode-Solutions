class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals:
            return []

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:

            last_start, last_end = merged[-1]

            # overlap
            if start <= last_end:
                merged[-1][1] = max(last_end, end)

            # no overlap
            else:
                merged.append([start, end])

        return merged
