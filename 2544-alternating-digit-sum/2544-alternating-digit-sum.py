class Solution:
    def alternateDigitSum(self, n: int) -> int:
        conv = str(n)
        ans = 0
        for i, d in enumerate(conv):
            if i % 2 == 0:
                factor = 1
            else:
                factor = -1
            
            ans += (int(d) * factor)

        
        return ans
    