# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.total = 0

        def dfs(node, current):

            if not node:
                return

            current = current * 10 + node.val

            # leaf node
            if not node.left and not node.right:
                self.total += current
                return

            dfs(node.left, current)
            dfs(node.right, current)

        dfs(root, 0)
        return self.total
