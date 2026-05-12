from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(s)):

            count[s[right]] += 1

            # shrink window if more than 2 distinct chars
            while len(count) > 2:

                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

            result = max(result, right - left + 1)

        return result
