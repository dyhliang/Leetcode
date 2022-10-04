# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.find_height(root.left), self.find_height(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  
        else:
            return abs(self.find_height(root.left) - self.find_height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)   
        