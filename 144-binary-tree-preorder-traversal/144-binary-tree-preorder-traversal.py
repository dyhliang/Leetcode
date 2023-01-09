# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root: Optional[TreeNode], res: list[int]):
        if not root:
            return
        
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
        