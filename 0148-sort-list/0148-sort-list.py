# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        curr = head
        while curr:
            hq.heappush(heap, curr.val)
            curr = curr.next
            
        sent = ListNode(None)
        if heap:
            p = hq.heappop(heap)
            new_head = ListNode(p)
            sent.next = new_head
        else:
            sent.next = None
        
        while heap:
            p = hq.heappop(heap)
            new_head.next = ListNode(p)
            new_head = new_head.next
            
        return sent.next
    