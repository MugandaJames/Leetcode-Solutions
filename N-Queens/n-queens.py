class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        result = []

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        board = [["."] * n for _ in range(n)]

        def backtrack(row):

            # placed all queens
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return

            for col in range(n):

                # invalid position
                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                # place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                board[row][col] = "Q"

                backtrack(row + 1)

                # remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

                board[row][col] = "."

        backtrack(0)

        return result
