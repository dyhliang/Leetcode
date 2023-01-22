class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occ = [0] * 26

        for i in range(len(s)):
            occ[ord(s[i]) - 97] += 1
            occ[ord(t[i]) - 97] -= 1

        for val in occ:
            if val != 0:
                return False

        return True
    