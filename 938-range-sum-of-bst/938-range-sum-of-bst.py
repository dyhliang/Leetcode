# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, res, node, low, high):
        if not node:
            return
        else:
            self.traverse(res, node.left, low, high)
            if node.val in range(low, high+1):
                res.append(node.val)
            self.traverse(res, node.right, low, high)
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        self.traverse(res, root, low, high)
        return sum(res)


    