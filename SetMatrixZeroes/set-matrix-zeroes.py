class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # update inner matrix
        for i in range(1, m):
            for j in range(1, n):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # update first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        # update first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
