class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occ = {}
        
        for i in range(len(magazine)):
            occ[magazine[i]] = 1 + occ.get(magazine[i], 0)
            
        for char in ransomNote:
            if char in occ and occ[char] > 0:
                occ[char] = occ.get(char, 0) - 1
            else:
                return False
            
        return True
    