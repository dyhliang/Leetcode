class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        r = 0
        longest = 1
        for i, n in enumerate(nums):
            if n > nums[r]:
                r = i
            else:
                longest = max(r - l + 1, longest)
                l = i
                r = i
              
        longest = max(r - l + 1, longest)
        return longest
            