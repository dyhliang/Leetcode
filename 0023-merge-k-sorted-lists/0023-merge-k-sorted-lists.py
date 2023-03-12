# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ll in lists:
            head = ll
            while head:
                hq.heappush(heap, head.val)
                head = head.next
        
        sent = ListNode(None)
        if heap:
            n = hq.heappop(heap)
            sent.next = ListNode(n)
        curr = sent.next
            
        while heap:
            n = hq.heappop(heap)
            curr.next = ListNode(n)
            curr = curr.next

        return sent.next
    