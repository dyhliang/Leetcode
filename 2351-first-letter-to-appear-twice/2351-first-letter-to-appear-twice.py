class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occ = {}   
        for char in s:
            occ[char] = 1 + occ.get(char, 0)
    
            if occ[char] == 2:
                return char
            