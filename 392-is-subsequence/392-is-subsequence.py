class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        subseq = ""
        
        if len(s) == 0:
            return True

        for i in range(len(t)):
            if s[j] == t[i]:
                subseq += s[j]
                j += 1

            if j == len(s) and len(subseq) < len(s):
                return False

            if subseq == s:
                return True

        return False
    