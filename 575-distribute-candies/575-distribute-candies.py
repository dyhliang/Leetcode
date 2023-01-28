class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = len(set(candyType))
        return min(len(candyType) // 2, types)