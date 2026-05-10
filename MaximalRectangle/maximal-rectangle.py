class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        def largestRectangle(hist):

            stack = []
            area = 0

            hist.append(0)  # sentinel

            for i in range(len(hist)):

                while stack and hist[i] < hist[stack[-1]]:

                    h = hist[stack.pop()]

                    right = i
                    left = stack[-1] if stack else -1

                    area = max(area, h * (right - left - 1))

                stack.append(i)

            hist.pop()  # remove sentinel
            return area

        for row in matrix:

            for j in range(n):

                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, largestRectangle(heights))

        return max_area
