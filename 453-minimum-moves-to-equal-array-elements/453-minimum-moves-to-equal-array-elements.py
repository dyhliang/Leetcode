class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        # [1,1,1] = 0, every value is the same
        # [1,2,7] = 
        
        nums.sort()
        total = sum(nums[1:])
        res = total - (nums[0] * len(nums[1:]))
        return res