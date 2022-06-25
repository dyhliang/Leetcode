class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pos = -1
        
        while pos * -1 < len(nums) - 1:
            if nums[pos-2] + nums[pos-1] > nums[pos]:
                return nums[pos] + nums[pos-1] + nums[pos-2]
            pos -= 1
        
        return 0
        