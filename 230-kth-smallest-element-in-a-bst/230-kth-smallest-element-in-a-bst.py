import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, res)
        heapq.heapify(res)
        
        while k > 1:
            heapq.heappop(res)
            k -= 1
            
        return res[0]
        
    def inorder(self, root: Optional[TreeNode], arr: list) -> list:
        # Performs inorder traversal to set up a list to be heapified
        if not root:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        