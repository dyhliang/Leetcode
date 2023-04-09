class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ = defaultdict(int)
        
        for char in s:
            occ[char] += 1
            
        return len(set(occ.values())) == 1