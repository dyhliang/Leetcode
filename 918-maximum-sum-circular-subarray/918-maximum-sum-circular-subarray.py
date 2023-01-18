class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        total = 0
        max_sum, min_sum = nums[0], nums[0]
        
        for num in nums:
            curr_max = max(curr_max, 0) + num
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min, 0) + num
            min_sum = min(min_sum, curr_min)
            total += num
            
        if total == min_sum:
            return max_sum
        else:
            return max(max_sum, total - min_sum)
            