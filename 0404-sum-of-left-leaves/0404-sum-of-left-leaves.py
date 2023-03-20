# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], check_left: int, lefts: list[int]):
        if not root:
            return
        
        if not root.left and not root.right:
            if check_left:
                lefts.append(root.val)
                
        self.traverse(root.left, True, lefts)
        self.traverse(root.right, False, lefts)
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        lefts = []
        self.traverse(root, False, lefts)
        return sum(lefts)
    