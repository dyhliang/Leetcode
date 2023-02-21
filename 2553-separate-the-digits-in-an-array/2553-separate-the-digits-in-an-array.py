class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            digits = [*str(n)]
            ans += digits
            
        ans = [int(d) for d in ans]
        return ans
    