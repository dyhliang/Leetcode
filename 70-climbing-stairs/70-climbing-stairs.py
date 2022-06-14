class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            prevprev = 1
            prev = 2
            total = 3
            curr = 3
            
            while curr < n:
                prevprev = prev
                prev = total
                total += prevprev
                curr += 1
            
            return total
                
        