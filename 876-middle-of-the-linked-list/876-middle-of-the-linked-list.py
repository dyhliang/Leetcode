# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        total = 0
        while curr:
            total += 1
            curr = curr.next
            
        curr = head
        count = 0
        while curr:
            if count == total // 2:
                return curr
            else:
                count += 1
                curr = curr.next
        

