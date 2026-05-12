class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        wordSet = set(wordDict)
        memo = {}

        def dfs(start):

            # Already computed
            if start in memo:
                return memo[start]

            # Reached end
            if start == len(s):
                return [""]

            sentences = []

            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in wordSet:

                    # Solve remaining suffix
                    rest = dfs(end)

                    for sub in rest:

                        if sub:
                            sentences.append(word + " " + sub)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)
