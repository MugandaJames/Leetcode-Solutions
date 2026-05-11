# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # Store inorder indices for fast lookup
        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.preorder_index = 0

        def helper(left, right):

            # No elements to construct
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            index = inorder_map[root_val]

            # Build left subtree
            root.left = helper(left, index - 1)

            # Build right subtree
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
