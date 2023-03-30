class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True

        def check_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(s, left, right - 1) or check_palindrome(s, left + 1, right)
            left += 1
            right -= 1
            
        return True
    