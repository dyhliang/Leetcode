# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels = []
        if not root:
            return 0
        
        def traverse(node, i):
            if len(levels) == i:
                levels.append([])
                
            levels[i].append(node.val)
            if node.left:
                traverse(node.left, i+1)
                
            if node.right:
                traverse(node.right, i+1)
                
            
        traverse(root, 0)
        return len(levels)
    