class Solution(object):
    def lengthOfLastWord(self, s):
        str_list = s.split()
        return len(str_list[-1])
        