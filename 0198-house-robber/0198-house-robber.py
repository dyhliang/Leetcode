class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * (n + 1)
        dp[n], dp[n-1] = 0, nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+2] + nums[i], dp[i+1])

        return dp[0]
        