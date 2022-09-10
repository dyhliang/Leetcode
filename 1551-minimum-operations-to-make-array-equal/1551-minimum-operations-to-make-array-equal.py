class Solution:
    def minOperations(self, n: int) -> int:
        # n = 1: 0 [1]
        # n = 2: 1 [1, 3]
        # n = 3: 2 [1, 3, 5]
        # n = 4: 4 [1, 3, 5, 7]
        # n = 5: 6 [1, 3, 5, 7, 9]
        # n = 6: 9 [1, 3, 5, 7, 9, 11]
        # n = 7: 12 [1, 3, 5, 7, 9, 11, 13]
        # n = 10: 25 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        # The pattern: Find the median, and add the distance from the median to 
        # each values at each index after(or before, but not both).
        # Also, n itself is conveniently the median.
        if n % 2 == 0:
            curr = n + 1
        else:
            curr = n
            
        ops = 0
        while curr <= (2 * n - 1):
            ops += (curr - n)
            curr += 2
            
        return ops