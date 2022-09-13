# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through l1 and l2 and append its digits casted as a str onto its own list
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
            
        # Join and reverse the digits for both lists, then cast into an int so we can 
        # use the normal + operation on ints to forgo using extra ifs or loops to carry
        num_1 = int(''.join(first_lst)[::-1])
        num_2 = int(''.join(sec_lst)[::-1])
        
        # Reverse the sum back since we want to start with ones digit in the LL
        # use a front sentinel and curr to make pointer assignments less confusing
        total = str(num_1 + num_2)[::-1]
        sentinel = ListNode(0)  # The extra 0 here won't be an issue as we can return sentinel.next to avoid it
        curr = sentinel
        for digit in total:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return sentinel.next
    