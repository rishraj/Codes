def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # derive what is needed from case analysis
    if not head:
        return head
    dhead = ListNode(-1)
    dhead.next = head
    l, tail, cur = 0, head, head
    while cur:
        l += 1
        tail = cur
        cur = cur.next
    k = k % l
    if not k:
        return head
    i, prev = l - k, dhead
    while i:
        prev = prev.next
        i -= 1
    tmp = dhead.next
    dhead.next = prev.next
    tail.next = tmp
    prev.next = None
    return dhead.next