class Solution:
    def checkIfPangram(self, s: str) -> bool:
        
        if len(s) < 26:
            return False
        
        no_dupes = "".join(set(str(s)))
        occ = {}
        
        for char in no_dupes:
            occ[char] = 1 + occ.get(char, 0)

        return len(occ.keys()) == 26
    