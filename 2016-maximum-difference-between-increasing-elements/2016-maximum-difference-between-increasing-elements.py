class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        helper = []
        max_diff = -1 
        for i, val in enumerate(nums[:len(nums)-1]):
            curr_diff = max(nums[i+1:]) - val
            max_diff = max(max_diff, curr_diff)
                
        if max_diff <= 0:
            return -1
        else:
            return max_diff