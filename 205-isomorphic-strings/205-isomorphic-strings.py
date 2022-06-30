class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        
        for pos in range(len(s)):
            # Map to hash table if neither character has been visited or used as a pair
            if s[pos] not in mappings.keys() and t[pos] not in mappings.values():
                mappings[s[pos]] = t[pos]
            elif s[pos] not in mappings.keys() and t[pos] in mappings.values():
                return False    # if s char hasn't been used but t char has
            elif s[pos] in mappings.keys() and t[pos] != mappings[s[pos]]:
                return False    # is s char has been used but t char isn't its matched pair
            
        return True
    