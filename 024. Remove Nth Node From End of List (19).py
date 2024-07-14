def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # soln. taking more than 1 pass of list
    # remove len(list) - n from the start
    """ dhead = ListNode(-1)  # dummy head is very very useful to deal with edge cases
    dhead.next = head
    cur, l = dhead, 0
    while cur.next:
        l += 1
        cur = cur.next
    dif, prev = l - n, dhead # prev is previous of node to be removed
    while dif:
        prev = prev.next
        dif -= 1
    prev.next = prev.next.next
    return dhead.next """
    
    # soln. taking a single pass
    # keep 2 pointers 'n' length apart
    dhead = ListNode(-1) # dummy head is very very useful to deal with edge cases
    dhead.next = head
    prev, cur = dhead, dhead
    while n:
        cur = cur.next
        n -= 1
    while cur.next:
        prev = prev.next
        cur = cur.next
    prev.next = prev.next.next
    return dhead.next