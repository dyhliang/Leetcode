# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root:
            res = self.traverse(root, targetSum, [], 0, [])
            return res
        else:
            return None
        
    
    def traverse(self, root: Optional[TreeNode], target: int, path: Optional[TreeNode], total: int, res):
        if not root:
            return
        else:
            path.append(root.val)
            if not root.left and not root.right:
                total = sum(path)
                if total == target:
                    valid_path = copy.deepcopy(path)
                    res.append(valid_path)
        
        self.traverse(root.left, target, path, total, res)
        self.traverse(root.right, target, path, total, res)
        path.pop()
        
        return res
        