class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        for i, char in enumerate(s):
            # Map to hash table if neither character has been visited or used as a pair
            if s[i] not in mappings.keys() and t[i] not in mappings.values():
                mappings[s[i]] = t[i]
            elif s[i] not in mappings.keys() and t[i] in mappings.values():
                return False    # if s char hasn't been used but t char has
            elif s[i] in mappings.keys() and t[i] != mappings[s[i]]:
                return False    # is s char has been used but t char isn't its matched pair
            
        return True
    