def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # set prev = None to handle the end of the reversed list
    prev, cur = None, head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev