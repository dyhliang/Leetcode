class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        psum = [nums[0]]
        for n in nums[1:]:
            psum.append(n + psum[-1])
            
        if min(psum) < 1:
            return abs(min(psum)) + 1
        else:
            return 1
    