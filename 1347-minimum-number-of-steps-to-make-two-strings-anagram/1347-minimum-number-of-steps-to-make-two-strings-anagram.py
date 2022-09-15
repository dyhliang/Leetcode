class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_hash = {}
        
        for char in s:
            s_hash[char] = 1 + s_hash.get(char, 0)
            
        count = 0
        for char in t:
            if char not in s_hash.keys() or s_hash[char] <= 0:
                count += 1
            else:
                s_hash[char] -= 1
                    
        return count
    