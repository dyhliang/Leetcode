class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = list(sorted(s))
        new_t = list(sorted(t))
        return new_s == new_t