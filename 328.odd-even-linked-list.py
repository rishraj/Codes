#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # did this purely by example anaysis (no use trying to understand this code after some time)
        
        # methodical soln in notebook (basically keep 2 pointers and a counter to
        # split the list to 2 separate lists and then join them)
        
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
    
# @lc code=end

