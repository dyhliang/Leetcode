class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = [*s]
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not chars[l].isalpha():
                l += 1
            elif not chars[r].isalpha():
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        
        res = "".join(chars)
        return res
    