# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.postorder_index = len(postorder) - 1

        def helper(left, right):

            if left > right:
                return None

            # Current root
            root_val = postorder[self.postorder_index]
            self.postorder_index -= 1

            root = TreeNode(root_val)

            index = inorder_map[root_val]

            # IMPORTANT:
            # Build right subtree first
            root.right = helper(index + 1, right)

            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
