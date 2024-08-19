#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # soln works, but is not the most elegant
        """ dhead, c = ListNode(-1), 0
        cur = dhead
        while l1 or l2 or c:
            if l1 and l2:
                s = l1.val + l2.val + c
                cur.next = ListNode(s % 10)
                cur = cur.next
                l1 = l1.next 
                l2 = l2.next
                c = s // 10
            elif l1:
                s = l1.val + c
                cur.next = ListNode(s % 10)
                cur = cur.next
                l1 = l1.next 
                c = s // 10
            elif l2:
                s = l2.val + c
                cur.next = ListNode(s % 10)
                cur = cur.next
                l2 = l2.next 
                c = s // 10
            elif c:
                cur.next = ListNode(c)
        return dhead.next """ 
        
        # pythonic way
        dhead = ListNode(-1)
        cur = dhead
        c = 0
        while l1 or l2 or c:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            s = l1_val + l2_val + c
            cur.next = ListNode(s % 10)
            cur = cur.next
            c = s // 10


            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dhead.next
    
# @lc code=end

