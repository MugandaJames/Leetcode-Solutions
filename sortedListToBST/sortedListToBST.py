# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        # Empty list
        if not head:
            return None

        # Single node
        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        prev.next = None

        # Middle becomes root
        root = TreeNode(slow.val)

        # Build subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
