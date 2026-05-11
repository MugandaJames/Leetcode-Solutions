# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        # Leaf node
        if not root.left and not root.right:
            return 1

        # If left is missing, go right only
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If right is missing, go left only
        if not root.right:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
