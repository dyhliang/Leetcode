class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        pos = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                pos += 1
                nums[pos] = nums[i]
        
        return pos + 1
    