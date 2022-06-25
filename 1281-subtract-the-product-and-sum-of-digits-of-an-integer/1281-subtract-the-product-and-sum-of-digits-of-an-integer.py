class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        product = 1
        total = 0
        for val in str_n:
            product *= int(val)
            total += int(val)
            
        return product - total
    