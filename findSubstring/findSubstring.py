from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        results = []

        # Start from 0 up to word_len - 1
        for i in range(word_len):
            left = i
            curr_counts = Counter()
            count = 0

            # Slide across the string in steps of word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j: j + word_len]

                if word in word_counts:
                    curr_counts[word] += 1
                    count += 1

                    # If we have more of 'word' than allowed, shrink from the left
                    while curr_counts[word] > word_counts[word]:
                        left_word = s[left: left + word_len]
                        curr_counts[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Check if we found a valid concatenation
                    if count == num_words:
                        results.append(left)
                else:
                    # Word not in list: reset the window
                    curr_counts.clear()
                    count = 0
                    left = j + word_len

        return results
