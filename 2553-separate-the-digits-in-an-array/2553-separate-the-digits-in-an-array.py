class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        conv = [str(n) for n in nums]
        ans = []
        
        for num in conv:
            digits = [*num]
            ans += digits
            
        ans = [int(d) for d in ans]
        return ans
    