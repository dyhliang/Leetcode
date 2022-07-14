# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        vals = []
        curr = head
        while curr:
            vals.append(curr)
            curr = curr.next
            
        return vals[len(vals) // 2]
