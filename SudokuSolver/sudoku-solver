class Solution(object):
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        # 1. Pre-process the board: record existing numbers and find empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c]) - 1
                    self.toggle_bit(rows, cols, boxes, r, c, val)
                else:
                    empty_cells.append((r, c))

        # 2. Start backtracking using the list of empty cells
        self.backtrack(board, empty_cells, 0, rows, cols, boxes)

    def toggle_bit(self, rows, cols, boxes, r, c, val):
        # Use bitwise OR to set the bit for that number
        mask = 1 << val
        rows[r] ^= mask
        cols[c] ^= mask
        boxes[(r // 3) * 3 + (c // 3)] ^= mask

    def backtrack(self, board, empty_cells, index, rows, cols, boxes):
        if index == len(empty_cells):
            return True
        
        r, c = empty_cells[index]
        box_idx = (r // 3) * 3 + (c // 3)
        
        # Get bits representing numbers already taken in this row, col, and box
        taken = rows[r] | cols[c] | boxes[box_idx]
        
        # Try digits 1-9 (0-8 index)
        for val in range(9):
            # Check if the val-th bit is NOT taken
            if not (taken & (1 << val)):
                board[r][c] = str(val + 1)
                self.toggle_bit(rows, cols, boxes, r, c, val)
                
                if self.backtrack(board, empty_cells, index + 1, rows, cols, boxes):
                    return True
                
                # Backtrack: Reset bit and board
                self.toggle_bit(rows, cols, boxes, r, c, val)
                board[r][c] = "."
                
        return False
