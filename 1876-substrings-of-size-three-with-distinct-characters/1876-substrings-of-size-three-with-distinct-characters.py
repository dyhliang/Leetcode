class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = []
        for i, trio in enumerate(s[0:len(s)-2]):
            trio = s[i:i+3]
            if len(set(trio)) == len(trio):
                res.append(trio)
        
        return len(res)
    