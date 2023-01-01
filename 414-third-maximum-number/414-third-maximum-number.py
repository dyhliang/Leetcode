import heapq as hq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        desc = sorted(nums)[::-1]
        seen = []
        
        for val in desc:
            if val not in seen:
                seen.append(val)
                
            if len(seen) == 3:
                return seen[-1]
            
        return seen[0]