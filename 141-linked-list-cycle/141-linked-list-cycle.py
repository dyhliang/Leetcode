# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        pos = 0
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
                curr = curr.next
    
        return False