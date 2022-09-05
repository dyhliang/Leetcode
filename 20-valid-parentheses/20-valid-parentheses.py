class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(",
                 "]": "[",
                 "}": "{"}
        helper = []
        
        for char in s:
            # This will check to see if the current character is a left char, if so append, if not we check =....
            if char in pairs.values():
                helper.append(char)
            else:
                # ...to see if its left counterpart is the same as the left char at top of the stack, if so pop as we found a pairing, if not, we're done and return False
                if helper and (helper[-1] == pairs[char]):
                    helper.pop()
                else:
                    return False

        # account for edge cases where we only find left chars, then just check to see if the stack is empty as valid pairs would reduce the the stack via pop()
        return len(helper) == 0
    