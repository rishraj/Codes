#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge2Lists(self, l1, l2):
        """ dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next """
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # merge half of len(lists) at a time like in merge sort
        # time = O(nlog(k))
        """ if len(lists) == 0: return None # edge case
        while len(lists) > 1:
            tmpLists = []
            for i in range(0, len(lists), 2): # merge lists in pair of 2
                l1 = lists[i]
                l2 = lists[i + 1] if i < len(lists)-1 else None
                tmpLists.append(self.merge2Lists(l1, l2))
            lists = tmpLists
        return lists[0] """
        
        # use minHeap of size k
        # time = O(nlog(k))
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node] # i is from 0 to k (used as unique identifier, otherwise error when heap compares 2 nodes if their val is same)
        heapq.heapify(heap)
        
        tail = dummy = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, (tail.next.val, i, tail.next))                
        return dummy.next
        
# @lc code=end

