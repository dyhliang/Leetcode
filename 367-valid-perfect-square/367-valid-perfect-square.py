class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = num ** (1/2)
        return int(root + 0.5) ** 2 == num
    