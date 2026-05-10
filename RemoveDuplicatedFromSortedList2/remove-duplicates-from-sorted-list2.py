class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # detect duplicates
            if curr.next and curr.val == curr.next.val:

                # skip all duplicates
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                # link prev to next distinct node
                prev.next = curr.next

            else:
                prev = prev.next

            curr = curr.next

        return dummy.next
