class Solution(object):
    def reverseWords(self, s):

        words = []
        n = len(s)
        i = 0

        while i < n:

            # skip spaces
            while i < n and s[i] == " ":
                i += 1

            if i >= n:
                break

            j = i

            while j < n and s[j] != " ":
                j += 1

            words.append(s[i:j])
            i = j

        return " ".join(words[::-1])
