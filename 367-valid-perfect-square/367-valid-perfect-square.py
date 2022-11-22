class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        closest_sq = int(num ** (1 / 2))
        return closest_sq ** 2 == num
    