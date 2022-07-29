class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = str(x)[::-1]
        return rev_x == str(x)
    