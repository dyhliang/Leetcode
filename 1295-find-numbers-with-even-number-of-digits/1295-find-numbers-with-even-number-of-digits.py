class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for val in nums:
            if len(str(val)) % 2 == 0:
                ans += 1
                
        return ans
    