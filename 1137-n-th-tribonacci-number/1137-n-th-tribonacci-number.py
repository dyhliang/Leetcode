class Solution:
    def tribonacci(self, n: int) -> int:
        table = [0, 1, 1]
        
        if n < 3:
            return table[n]
        
        for val in range(3, n+1):
            table.append(table[-1] + table[-2] + table[-3])
        
        return table[-1]