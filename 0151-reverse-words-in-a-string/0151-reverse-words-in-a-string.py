class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        curr_word = ""
        for char in s:
            if char == " ":
                stack.append(curr_word)
                curr_word = ""
            else:
                curr_word += char
                
        stack.append(curr_word)
            
        res = ""
        while stack:
            word = stack.pop()
            if word != "":
                res += (word + " ")
                
        return res[:-1]