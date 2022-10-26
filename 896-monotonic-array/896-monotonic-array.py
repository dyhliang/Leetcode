class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
    
        # A list of less than 3 elements is always monotonic
        if len(nums) < 3:
            return True
        
        prev = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            curr = nums[i] - nums[i-1]
            
            if (prev < 0 and curr > 0) or (prev > 0 and curr < 0):
                return False
            
            if curr != 0:
                prev = curr
            
        return True
    