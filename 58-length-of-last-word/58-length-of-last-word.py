class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        conv_list = s.split(" ")[::-1]
        for w in conv_list:
            if w.isalpha():
                return len(w)
            