class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0 + k - 1
        min_diff = float(inf)
        
        while r < len(nums):
            min_diff = min(min_diff, nums[r] - nums[l])
            l += 1
            r += 1
            
        return min_diff
    