class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        result = []

        def backtrack(start, path):

            # if we have 4 parts and used all digits
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return

            # invalid state
            if len(path) == 4:
                return

            for length in range(1, 4):  # 1 to 3 digits

                if start + length > len(s):
                    break

                part = s[start:start + length]

                # leading zero check
                if part.startswith("0") and len(part) > 1:
                    continue

                # range check
                if int(part) > 255:
                    continue

                path.append(part)

                backtrack(start + length, path)

                path.pop()

        backtrack(0, [])

        return result
