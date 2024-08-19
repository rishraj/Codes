#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        l1_head, l2_head = ListNode(-1), ListNode(-1) # dummy heads
        l1_tail, l2_tail = l1_head, l2_head
        while cur:
            if cur.val < x:
                l1_tail.next = cur
                l1_tail = l1_tail.next
            else:
                l2_tail.next = cur
                l2_tail = l2_tail.next
            cur = cur.next
        l1_tail.next = l2_head.next
        l2_tail.next = None
        return l1_head.next
    
# @lc code=end

