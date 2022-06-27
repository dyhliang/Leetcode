class Solution:
    def minPartitions(self, n: str) -> int:
        digits = [char for char in n]
        return max(digits)