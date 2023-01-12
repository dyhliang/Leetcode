class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = deque([])
        for char in s:
            if char.isalnum():
                new_s.append(char)

        while len(new_s) > 1:
            left = new_s.popleft()
            right = new_s.pop()
            
            if left.lower() != right.lower():
                return False
            
        return True
        