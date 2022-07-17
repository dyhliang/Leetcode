# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            temp = curr.next    
            
            curr.next = temp.next  

            if curr == head:
                head = temp
                temp.next = curr
            else:
                temp.next = curr
                prev.next = temp
                
            prev = curr
            if curr.next:
                curr = curr.next
            
        return head
    