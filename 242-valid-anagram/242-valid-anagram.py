class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        convert_s = sorted([*s])
        convert_t = sorted([*t])
        
        return convert_s == convert_t
    