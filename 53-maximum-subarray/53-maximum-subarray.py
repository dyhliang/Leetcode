class Solution:
    def maxSubArray(self, nums):
        # Use Kadane's algorithm
        curr_arr = nums[0]
        max_arr = curr_arr

        for pos in range(1, len(nums)):  
            if curr_arr < 0:
                curr_arr = 0
    
            curr_arr += nums[pos]
            
            if curr_arr > max_arr:
                max_arr = curr_arr
                    
        return max_arr