# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # Since we don't have access to the prev node, we need to modify the current node's
        # value in place to the value of its next node, and its next pointer so that it's pointing to the node 2 spots over to its right.
        node.val = node.next.val
        node.next = node.next.next