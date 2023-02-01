class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
            # Then updates the value at the prev index to reflect the highest 
            # money amt stolen up to that point
            dp[i-1] = max(dp[i-1], dp[i-2])

        return max(dp[-2], dp[-1])