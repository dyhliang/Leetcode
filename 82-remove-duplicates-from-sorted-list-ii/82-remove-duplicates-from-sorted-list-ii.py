# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        # Use a set to store dupe values seen for checking head and tail later
        dupes = set()
        curr = head
        prev = head
        
        while curr.next:
            if curr.val == curr.next.val:
                dupes.add(curr.val)
                curr.next = curr.next.next
            else:
                # Once all of duplicates that follow curr node are removed, remove the curr node as well
                if curr.val in dupes:
                    prev.next = curr.next
                else:
                    prev = curr
                
                curr = curr.next
                
        # If the last value is a dupe, make sure to remove as well
        if curr.val in dupes:
            prev.next = curr.next
            
        # Come back and shift the head if was a dupe value
        if head.val in dupes:
            head = head.next
        
        return head
    