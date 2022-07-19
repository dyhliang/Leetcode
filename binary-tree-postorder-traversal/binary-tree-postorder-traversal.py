# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postTraverse(root, res)
        return res
    
    def postTraverse(self, root, res):
        if not root:
            return
        
        self.postTraverse(root.left, res)
        self.postTraverse(root.right, res)
        res.append(root.val)
    