# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        first_lst = []
        while curr:
            first_lst.append(str(curr.val))
            curr = curr.next
            
        curr = l2
        sec_lst = []
        while curr:
            sec_lst.append(str(curr.val))
            curr = curr.next
            
        num_1 = int(''.join(first_lst[::-1]))
        num_2 = int(''.join(sec_lst[::-1]))
        
        total = str(num_1 + num_2)[::-1]
        
        head = ListNode(0)
        curr = head
        for digit in total:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return head.next
    