class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        rights = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    rights += 1
        
        return len(stack) + rights
    