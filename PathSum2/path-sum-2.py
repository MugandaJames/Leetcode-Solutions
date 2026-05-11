# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        result = []
        path = []

        def dfs(node, remaining):

            if not node:
                return

            # Add current node
            path.append(node.val)

            # Check leaf + valid sum
            if not node.left and not node.right and remaining == node.val:
                result.append(list(path))  # copy path

            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            # Backtrack
            path.pop()

        dfs(root, targetSum)
        return result
