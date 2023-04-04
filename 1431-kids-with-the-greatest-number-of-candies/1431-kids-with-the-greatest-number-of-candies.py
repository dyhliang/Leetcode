class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_amt = max(candies)
        res = [c + extraCandies >= max_amt for c in candies]
        return res