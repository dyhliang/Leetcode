class Solution(object):
    def singleNumber(self, nums):

        no_dupes = set(nums)
    
        for val in no_dupes:
            if nums.count(val) == 1:
                return val
        