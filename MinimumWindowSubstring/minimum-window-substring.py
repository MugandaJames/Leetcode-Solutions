from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):

            char = s[right]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            # shrink window
            while have == need_count:

                # update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        left_idx, right_idx = res

        return s[left_idx:right_idx + 1] if res_len != float("inf") else ""
