class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) == 0:
            return []
        
        new_nums = []
        new_k = k % len(nums)   # updates k to move minimally


        # len(nums) - new_k for scenarios where 
        new_nums[0:new_k] = nums[len(nums) - new_k: len(nums)]
        new_nums[new_k:] = nums[0:len(nums) - new_k]
        nums[:] = new_nums