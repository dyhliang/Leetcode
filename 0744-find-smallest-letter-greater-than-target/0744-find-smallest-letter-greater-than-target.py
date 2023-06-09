class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        occ = [0] * 26
        occ[ord(target) - 97] += 1
        
        for c in letters:
            occ[ord(c) - 97] += 1

        for i, n in enumerate(occ):
            
            if i + 97 > ord(target) and n != 0:
                return chr(i + 97)
            
        return letters[0]
            