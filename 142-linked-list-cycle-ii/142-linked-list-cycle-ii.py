# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        visited = []
        while curr:
            if curr in visited:
                return curr
            else:
                visited.append(curr)
                curr = curr.next
            
        return None
            