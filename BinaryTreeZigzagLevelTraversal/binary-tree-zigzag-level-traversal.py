from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:

            level = []
            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Reverse every other level
            if not left_to_right:
                level.reverse()

            result.append(level)

            # Flip direction
            left_to_right = not left_to_right

        return result
