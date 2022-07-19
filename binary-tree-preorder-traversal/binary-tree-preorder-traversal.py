# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preTraverse(root, res)
        return res
        
    def preTraverse(self, root: Optional[TreeNode], res: list[int]):
        
        if not root:
            return
        
        res.append(root.val)
        self.preTraverse(root.left, res)
        self.preTraverse(root.right, res)
        return
        