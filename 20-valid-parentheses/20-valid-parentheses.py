class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
                 "]": "[",
                 "}": "{"}

        helper = []
        for char in s:
            if char in pairs:
                if helper and helper[-1] == pairs[char]:
                    top = helper.pop()
                else:
                    return False
            else:
                helper.append(char)
            
        return len(helper) == 0
    