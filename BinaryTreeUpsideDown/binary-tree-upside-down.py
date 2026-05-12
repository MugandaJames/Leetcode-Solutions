class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)

        root_left = root.left
        root_right = root.right

        # flip connections
        root_left.left = root_right
        root_left.right = root

        # cut old links
        root.left = None
        root.right = None

        return new_root
