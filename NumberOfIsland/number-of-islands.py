class Solution:

  def numIslands(self, grid: List[List[str]]) -> bool:
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
      # Base case: out of bounds or water ('0')
      if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
        return

      # Mark cell as visited by sinking it
      grid[r][c] = '0'

      # Traverse 4 adjacent directions
      dfs(r + 1, c)  # Down
      dfs(r - 1, c)  # Up
      dfs(r, c + 1)  # Right
      dfs(r, c - 1)  # Left

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1':
          islands += 1
          dfs(r, c)  # Sink the connected island

    return islands
