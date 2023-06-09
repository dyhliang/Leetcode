class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        occ = [0] * 26
        occ[ord(target) - 97] += 1
        
        for c in letters:
            occ[ord(c) - 97] += 1

        seen = False
        
        for i, n in enumerate(occ):
            
            if seen and n != 0:
                return chr(i + 97)
            
            if i == (ord(target) - 97):
                seen = True
            
        return letters[0]
            