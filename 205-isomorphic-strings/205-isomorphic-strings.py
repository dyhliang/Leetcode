class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        
        for pos in range(len(s)):
            if s[pos] not in mappings.keys() and t[pos] not in mappings.values():
                mappings[s[pos]] = t[pos]
            elif s[pos] not in mappings.keys() and t[pos] in mappings.values():
                return False
            elif s[pos] in mappings.keys() and t[pos] != mappings[s[pos]]:
                return False
            
        return True
    