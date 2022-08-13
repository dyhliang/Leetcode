class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occ = {}
        for val in nums:
            occ[val] = 1 + occ.get(val, 0)
        
        nums.sort()
        
        for i in range(len(nums)-1, -1, -1):
            if occ[nums[i]] == 1:
                return nums[i]
            
        return -1
    