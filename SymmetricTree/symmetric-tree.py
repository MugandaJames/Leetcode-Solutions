# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def isMirror(left, right):

            # Both nodes are empty
            if not left and not right:
                return True

            # One is empty, one is not
            if not left or not right:
                return False

            # Values must match
            if left.val != right.val:
                return False

            # Check mirrored children
            return (
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)
