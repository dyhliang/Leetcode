class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = sum(nums[1:])
        
        if left == right:
            return 0
        
        for i in range(1, len(nums)):
            right -= nums[i]
            left += nums[i-1]
            
            if left == right:
                return i
        return -1
            