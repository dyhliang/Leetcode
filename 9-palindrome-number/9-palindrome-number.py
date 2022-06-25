class Solution(object):
    def isPalindrome(self, x):
        rev_x = str(x)[::-1]
        return rev_x == str(x)
    