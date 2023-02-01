class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            diff = len(text1) - len(text2)
            text2 += (diff * "_")
        elif len(text2) > len(text1):
            diff = len(text2) - len(text1)
            text1 += (diff * "_")

        n = len(text1) + 1
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
    