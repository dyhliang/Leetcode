class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, subarrs = 0, 0
        
        for n in nums:
            if n == 0:
                subarrs += 1
            else:
                subarrs = 0
            
            ans += subarrs
            
        return ans
    