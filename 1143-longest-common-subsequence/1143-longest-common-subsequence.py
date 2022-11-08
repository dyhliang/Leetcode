class Solution:
    def longestCommonSubsequence(self, dna1: str, dna2: str) -> int:
        # Bottom up approach
        len_1, len_2 = len(dna1), len(dna2)
        memo = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]

        for i in range(len_1 + 1):
            for j in range(len_2 + 1):
                if i == 0 or j == 0:
                    memo[i][j] = 0
                elif dna1[i - 1] == dna2[j - 1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        return memo[len_1][len_2]
