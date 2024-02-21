class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i > -1:
            if s[i] != " ":
                length += 1
            
            if length > 0 and s[i] == " ":
                return length
            
            i -= 1
            
        return length