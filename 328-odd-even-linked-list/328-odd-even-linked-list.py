# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        even_sent = ListNode(None)
        odd_sent = ListNode(None)
        even_curr, odd_curr = even_sent, odd_sent

        while head:
            if count % 2 == 0:
                even_curr.next = ListNode(head.val)
                even_curr = even_curr.next
            else:
                odd_curr.next = ListNode(head.val)
                odd_curr = odd_curr.next
            
            count += 1
            head = head.next
            
        odd_curr.next = even_sent.next
        
        return odd_sent.next