class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) > 0:
            new_nums = []
            new_k = k % len(nums)

            if new_k < len(nums):
                new_nums[0:new_k] = nums[len(nums) - new_k: len(nums)]
                new_nums[new_k:] = nums[0:len(nums) - new_k]
                nums[:] = new_nums
            elif new_k > 0:
                new_nums[0:new_k] = nums[new_k + 1:]
                new_nums[new_k:] = nums[0:new_k + 1]
                nums[:] = new_nums