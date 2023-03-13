# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        # Base case is mirror when neither tree have nodes
        if not n1 and not n2:
            return True
        
        if not n1 or not n2:
            return False
        
        return (n1.val == n2.val) and self.isMirror(n1.right, n2.left) and self.isMirror(n1.left, n2.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    