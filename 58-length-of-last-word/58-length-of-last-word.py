class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        conv_list = s.split()
        return len(conv_list[-1])
            