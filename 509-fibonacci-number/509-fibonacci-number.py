class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:      # Base case 
            return n
        
        return self.fib(n-1) + self.fib(n-2)
