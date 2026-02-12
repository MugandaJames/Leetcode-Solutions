class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0  # empty needle → return 0

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):  # slide window
            if haystack[i:i+m] == needle:
                return i
        return -1
