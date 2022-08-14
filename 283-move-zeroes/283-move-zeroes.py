class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[last_nonzero] = nums[i]
                last_nonzero += 1
        
        for i in range(last_nonzero, len(nums)):
            nums[i] = 0
            