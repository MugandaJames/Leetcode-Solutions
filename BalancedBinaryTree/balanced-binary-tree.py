# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def height(node):

            if not node:
                return 0

            left_height = height(node.left)

            # Left subtree already unbalanced
            if left_height == -1:
                return -1

            right_height = height(node.right)

            # Right subtree already unbalanced
            if right_height == -1:
                return -1

            # Current node unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return height(root) != -1
