class Solution:
    def firstUniqChar(self, s: str) -> int:
        occ = {}   
        for char in s:
            occ[char] = 1 + occ.get(char, 0)
    
        for i in range(len(s)):
            if occ[s[i]] == 1:
                return i
        return -1
            