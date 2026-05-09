class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next or k == 0:
            return head

        # 1. find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # 2. connect to form a circle
        tail.next = head

        # 3. effective rotations
        k = k % length
        steps_to_new_head = length - k

        new_tail = head

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # 4. break the circle
        new_tail.next = None

        return new_head
