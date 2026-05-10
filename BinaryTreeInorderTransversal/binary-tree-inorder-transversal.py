class Solution(object):
    def inorderTraversal(self, root):

        result = []
        stack = []
        curr = root

        while curr or stack:

            # go left as deep as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)

            curr = curr.right

        return result
