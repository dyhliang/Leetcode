class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for r in grid:
            for c in reversed(r):
                if c < 0:
                    count += 1
                    
        return count
    