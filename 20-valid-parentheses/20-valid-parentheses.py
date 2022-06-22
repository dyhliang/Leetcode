class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
                 "]": "[",
                 "}": "{"}
        helper = []
        for char in s:
            if char in pairs:
                # if the stack is not empty and the top of the stack == the value to the key, pop
                # else, return
                if helper and (helper[-1] == pairs[char]):
                    top = helper.pop()
                else:
                    return False
            else:
                # appends the left bracket onto stack
                helper.append(char)
            
        return len(helper) == 0
    