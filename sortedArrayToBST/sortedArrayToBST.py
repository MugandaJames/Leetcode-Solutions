# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def build(left, right):

            if left > right:
                return None

            # Middle element
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            # Left subtree
            root.left = build(left, mid - 1)

            # Right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
