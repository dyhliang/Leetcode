class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            prevprev = 0
            prev = 1
            total = 1
            curr = 2
            
            while curr < n:
                prevprev = prev
                prev = total
                total += prevprev
                curr += 1
            
            return total