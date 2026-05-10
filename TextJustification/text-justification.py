class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        result = []
        i = 0

        while i < len(words):

            # determine line range
            line_length = len(words[i])
            j = i + 1

            while (j < len(words) and
                   line_length + len(words[j]) + (j - i) <= maxWidth):

                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            line = ""

            # last line OR single word
            if j == len(words) or num_words == 1:

                for k in range(i, j):

                    line += words[k]

                    if k < j - 1:
                        line += " "

                # pad remaining spaces
                line += " " * (maxWidth - len(line))

            else:

                gaps = num_words - 1

                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                for k in range(i, j - 1):

                    line += words[k]

                    spaces = spaces_per_gap

                    # leftmost gaps get extra space
                    if extra_spaces > 0:
                        spaces += 1
                        extra_spaces -= 1

                    line += " " * spaces

                line += words[j - 1]

            result.append(line)

            i = j

        return result
