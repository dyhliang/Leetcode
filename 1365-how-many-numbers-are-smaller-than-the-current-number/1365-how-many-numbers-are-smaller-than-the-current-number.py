class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table = {}
        sorted_nums = sorted(nums, reverse=True)
        count = len(nums) - 1
        
        for i, val in enumerate(sorted_nums):
            table[val] = count
            count -= 1
            
        res = []
        for val in nums:
            res.append(table[val])
        
        return res
    