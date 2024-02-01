class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split(" ")        
        res = ""
        while stack:
            word = stack.pop()
            if word != "":
                res += (word + " ")
                
        return res[:-1]