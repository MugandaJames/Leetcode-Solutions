from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(set)
        level = {beginWord}
        found = False
        visited = set()

        while level and not found:

            next_level = set()
            visited |= level

            for word in level:

                for i in range(len(word)):

                    for c in "abcdefghijklmnopqrstuvwxyz":

                        nxt = word[:i] + c + word[i+1:]

                        if nxt in wordSet and nxt not in visited:

                            if nxt == endWord:
                                found = True

                            next_level.add(nxt)
                            parents[nxt].add(word)

            level = next_level

        # backtracking
        res = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                res.append(path[::-1])
                return

            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        if found:
            dfs(endWord)

        return res
