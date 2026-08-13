class Solution:

  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    shifts = 0
    # Keep shifting right until both numbers match (finding common prefix)
    while left < right:
      left >>= 1
      right >>= 1
      shifts += 1

    # Shift left back by the number of cleared bits
    return left << shifts
