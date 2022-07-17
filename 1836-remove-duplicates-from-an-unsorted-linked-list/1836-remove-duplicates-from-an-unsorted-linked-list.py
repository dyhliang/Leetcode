# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        hash_t = {}
        sent = ListNode(None)
        sent.next = head
        prev = sent        
        curr = head
        
        while curr:
            hash_t[curr.val] = 1 + hash_t.get(curr.val, 0)
            curr = curr.next
        
        curr = head
        while curr:
            if hash_t[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sent.next