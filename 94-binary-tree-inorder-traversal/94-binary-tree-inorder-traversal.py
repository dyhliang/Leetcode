# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, res, node):
        if not node:
            return
        else:
            self.traverse(res, node.left)
            res.append(node.val)
            self.traverse(res, node.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(res, root)
        return res
