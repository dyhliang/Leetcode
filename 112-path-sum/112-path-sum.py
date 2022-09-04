# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], arr: list, total: int) -> list:
        
        if not root:
            return
        else:
            total += root.val
        
        self.traverse(root.left, arr, total)
        self.traverse(root.right, arr, total)
        
        # Works like postorder traversal
        if not root.left and not root.right:
            arr.append(total)
            
        return arr
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root:
            res = self.traverse(root, [], 0)
            return targetSum in res
