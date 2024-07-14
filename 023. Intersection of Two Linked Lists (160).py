def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # space = O(max(lenA, lenB)) soln.
    # store all references of a list in a set and check the second list
    
    """ s = set()
    cur = headA
    while cur:
        s.add(cur)
        cur = cur.next
    cur = headB
    while cur:
        if cur in s:
            return cur
        cur = cur.next
    return None     """
    
    
    # space = O(1) soln.
    def get_length(head): # fn w/i fn is generally bad practise :P
        cur, res = head, 0
        while cur:
            res += 1
            cur = cur.next
        return res
    
    len_a = get_length(headA)
    len_b = get_length(headB)
    dif = abs(len_a - len_b)
    cur_a, cur_b = headA, headB
    while dif:
        if len_a > len_b:
            cur_a = cur_a.next
        else:
            cur_b = cur_b.next
        dif -= 1
    while cur_a:
        if cur_a == cur_b:
            return cur_a
        cur_a = cur_a.next
        cur_b = cur_b.next
    return None