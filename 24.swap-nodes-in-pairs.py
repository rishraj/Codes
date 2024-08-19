#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = ListNode(-1) # here dummy node helps to tackle edge cases of empty and 1 element lists
        dhead.next, cur = head, dhead
        
        # keep repairing connections of 3 nodes iteratively (below relations derived by case analysis)
        while cur.next and cur.next.next:
            prev = cur.next
            cur.next = cur.next.next
            cur = cur.next
            tmp = cur.next
            cur.next = prev
            prev.next = tmp
            cur = cur.next
        return dhead.next
    
# @lc code=end

