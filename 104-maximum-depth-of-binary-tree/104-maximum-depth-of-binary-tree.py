# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        curr = root
        if not root:
            return 0

        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)

        return max(left_d + 1, right_d + 1)
