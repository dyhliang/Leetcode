class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occ = {}
        for i in range(len(nums)):
            occ[nums[i]] = 1 + occ.get(nums[i], 0)
            if occ[nums[i]] == 2:
                return nums[i]