class Solution:
    def alternateDigitSum(self, n: int) -> int:
        conv = str(n)
        ans = 0
        for i, d in enumerate(conv):
            if i % 2 == 0:
                ans += int(d)
            else:
                ans -= int(d)
        
        return ans
    