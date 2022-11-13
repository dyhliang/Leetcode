class Solution:
    def reverseWords(self, s: str) -> str:
        no_spaces = (s.split(" "))
        no_spaces.reverse()
        res = ""
        
        for word in no_spaces:
            if word != "":
                res += (word + " ")
                
        return res[:-1]
        