class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero = 0
        # Modify in place, only need to keep this variable so that this will be the 
        # starting point for the ensuing array to change all elements there and onwards
        # to 0.
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[last_nonzero] = nums[i]
                last_nonzero += 1
        
        for i in range(last_nonzero, len(nums)):
            nums[i] = 0
            