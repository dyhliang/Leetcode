class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        res = ""
        for i, c in enumerate(word):
            prefix += c
            if c == ch:
                res = prefix[::-1] + word[i+1:]
                return res
        
        return word
    