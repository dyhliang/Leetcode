class Solution:
    def maxPower(self, s: str) -> int:
        stack = []
        longest = 1
        
        for char in s:
            if not stack or stack[-1] == char:
                stack.append(char)
            else:
                longest = max(longest, len(stack))
                stack = [char]
        
        longest = max(longest, len(stack))
        return longest