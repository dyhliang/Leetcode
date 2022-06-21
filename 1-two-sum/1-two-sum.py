class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        for pos, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], pos]
            
            prev[n] = pos
