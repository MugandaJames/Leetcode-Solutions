from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:

            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):

                for c in "abcdefghijklmnopqrstuvwxyz":

                    nxt = word[:i] + c + word[i+1:]

                    if nxt in wordSet:
                        wordSet.remove(nxt)
                        queue.append((nxt, steps + 1))

        return 0
