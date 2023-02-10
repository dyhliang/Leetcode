class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2, 3]
        
        for val in range(4, n+1):
            steps = memo[-2] + memo[-1]
            memo.append(steps)
            
        return memo[n]
    