class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Want the maximum area between two lines, where the rectangle is 
        # formed via: length = height of lower line, width = distance between
        # the indices of the two selected lines
        # Strategy: Two Pointers - always move pointer of lower line
        
        n = len(height)
        left = 0
        right = n - 1
        max_area = -float('inf')

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(curr_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area