class Solution:
    def reverseWords(self, s: str) -> str:
        no_spaces = (s.split(" "))
        res = ""
        
        for i in range(len(no_spaces)-1, -1, -1):
            if no_spaces[i] != "":
                res += (no_spaces[i] + " ")
                
        return res[:-1]
        