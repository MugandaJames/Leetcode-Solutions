class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []

        def build(l, r):

            if l > r:
                return [None]

            trees = []

            for i in range(l, r + 1):

                left_trees = build(l, i - 1)
                right_trees = build(i + 1, r)

                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(i)
                        root.left = left
                        root.right = right

                        trees.append(root)

            return trees

        return build(1, n)
