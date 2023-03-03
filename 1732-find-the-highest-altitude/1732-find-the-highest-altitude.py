class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heights = [0]
        i = 0
        
        for val in gain:
            n = heights[i] + val
            heights.append(n)
            i += 1
            
        return max(heights)
    