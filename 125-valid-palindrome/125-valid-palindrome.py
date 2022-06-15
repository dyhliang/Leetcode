class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [char for char in s.lower() if char.isalnum()]
        
        return res == res[::-1]