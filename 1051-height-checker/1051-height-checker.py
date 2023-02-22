class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted([val for val in heights])
        ans = 0
        
        for i, val in enumerate(new_heights):
            if new_heights[i] != heights[i]:
                ans += 1
                
        return ans
    