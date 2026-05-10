class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []  # stores indices
        max_area = 0

        heights.append(0)  # sentinel to flush stack

        for i in range(len(heights)):

            # maintain increasing stack
            while stack and heights[i] < heights[stack[-1]]:

                h = heights[stack.pop()]

                # right boundary
                right = i

                # left boundary
                left = stack[-1] if stack else -1

                area = h * (right - left - 1)

                max_area = max(max_area, area)

            stack.append(i)

        return max_area
