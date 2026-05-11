# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Empty tree
        if not root:
            return 0

        # Depth of left subtree
        left_depth = self.maxDepth(root.left)

        # Depth of right subtree
        right_depth = self.maxDepth(root.right)

        # Current depth
        return 1 + max(left_depth, right_depth)
