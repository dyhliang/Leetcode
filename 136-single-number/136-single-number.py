class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        no_dupes = set(nums)
    
        for val in no_dupes:
            if nums.count(val) == 1:
                return val
        