class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head_even = head.next
        cur = head
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            if cur.next:
                cur = cur.next
                tmp.next = cur.next
        cur.next = head_even
        return head