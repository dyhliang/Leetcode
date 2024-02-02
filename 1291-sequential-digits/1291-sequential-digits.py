class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dp = [['0' for i in range(9)] for j in range(9)]
        res = []

        for i, row in enumerate(dp):
            for j, col in enumerate(row):
                if j == i:
                    dp[i][j] = str(i + 1)
                else:
                    if j > i:
                        dp[i][j] = dp[i][j-1] + str(int(dp[i][j-1][-1]) + 1)

        for row in dp:
            for col in row:
                if int(col) in range(low, high+1):
                    res.append(int(col))

        sorted_res = sorted(res)
        return sorted_res