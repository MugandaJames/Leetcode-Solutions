class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            # Check if there are k nodes left
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next  # less than k nodes → done

            # Reverse k nodes
            curr = prev.next
            next_group = tail.next
            # detach group
            tail.next = None
            prev.next = self.reverseList(curr)
            curr.next = next_group  # connect reversed group back

            # Move prev to the end of the reversed group
            prev = curr

        return dummy.next

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
