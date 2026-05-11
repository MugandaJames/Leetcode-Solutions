# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_sum = float('-inf')

        def dfs(node):

            if not node:
                return 0

            # ignore negative paths (take 0 instead)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # best path THROUGH current node
            current = node.val + left + right

            self.max_sum = max(self.max_sum, current)

            # return best single branch upward
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
