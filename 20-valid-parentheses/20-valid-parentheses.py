class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = [s[0]]
        
        for char in s[1:]:
            if char not in pair.keys():
                stack.append(char)
            else:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    stack.append(char)
                    
        return len(stack) == 0
    