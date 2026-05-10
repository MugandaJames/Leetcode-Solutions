class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # move prev to node before left
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # reverse sublist
        for _ in range(right - left):

            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
