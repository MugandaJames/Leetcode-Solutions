class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next
