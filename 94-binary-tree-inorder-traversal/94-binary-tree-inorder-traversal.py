# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, res: list, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.traverse(res, node.left)
        res.append(node.val)
        self.traverse(res, node.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(res, root)
        return res
