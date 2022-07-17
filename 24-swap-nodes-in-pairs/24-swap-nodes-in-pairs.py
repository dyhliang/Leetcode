# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            temp = curr.next    # temp = 2
            
            curr.next = temp.next  # 2 -> 1 -> 3

            if curr == head:
                head = temp
            else:
                temp.next = curr
                prev.next = temp
                
            temp.next = curr
            prev = curr
            if curr.next:
                curr = curr.next
            
        return head