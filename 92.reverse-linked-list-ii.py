#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dhead = ListNode(-1)
        dhead.next, prev_left = head, dhead
        
        # going to the required left position
        for i in range(l - 1):
            prev_left = prev_left.next
        left = prev_left.next
        
        # reversing the required pointers
        prev, cur = left, left.next
        for i in range(r - l):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # correcting the remaining pointers
        prev_left.next = prev
        left.next = cur
        
        return dhead.next
    
# @lc code=end

