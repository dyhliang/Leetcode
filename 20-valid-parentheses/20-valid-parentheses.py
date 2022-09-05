class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
                 "]": "[",
                 "}": "{"}
        helper = []
        for char in s:
            if char in pairs.values():
                helper.append(char)
            else:
                if helper and (helper[-1] == pairs[char]):
                    helper.pop()
                else:
                    return False


        return len(helper) == 0
    