# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], arr: list[int]):
        if not root:
            return
            
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        self.inorder(root, arr)
        seen = []
        
        if arr:
            for val in arr:
                if k - val in seen:
                    return True
                else:
                    seen.append(val)
        else:
            return False
    