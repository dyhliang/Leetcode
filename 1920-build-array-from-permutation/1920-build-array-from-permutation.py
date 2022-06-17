class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_list = [nums[nums[i]] for i in range(len(nums))]
        return new_list