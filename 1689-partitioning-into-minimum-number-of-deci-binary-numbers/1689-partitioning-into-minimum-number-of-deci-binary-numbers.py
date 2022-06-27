class Solution:
    def minPartitions(self, n: str) -> int:
        # we just need the highest digit, therefore we would need at least that many
        # 1's to build (digit * the place value of that digit)
        digits = [char for char in n]
        return max(digits)
    