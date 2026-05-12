from collections import defaultdict

class Solution(object):

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxPoints(self, points):

        n = len(points)
        if n <= 2:
            return n

        res = 0

        for i in range(n):

            slopes = defaultdict(int)
            same = 1
            best = 0

            x1, y1 = points[i]

            for j in range(i + 1, n):

                x2, y2 = points[j]

                # duplicate point
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1

                g = self.gcd(dx, dy)
                dx //= g
                dy //= g

                # normalize direction
                if dx < 0:
                    dx *= -1
                    dy *= -1

                slopes[(dx, dy)] += 1
                best = max(best, slopes[(dx, dy)])

            res = max(res, best + same)

        return res
