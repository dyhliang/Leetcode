class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        high = 0
        for val in gain:
            curr = prev + val
            high = max(high, curr)
            prev = curr
            
        return high
    