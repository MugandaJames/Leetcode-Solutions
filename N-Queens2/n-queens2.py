class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        result = [0]

        def backtrack(row):

            # valid arrangement found
            if row == n:
                result[0] += 1
                return

            for col in range(n):

                # attacked position
                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                # place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # remove queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result[0]
