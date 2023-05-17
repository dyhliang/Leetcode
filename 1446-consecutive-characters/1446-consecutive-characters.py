class Solution:
    def maxPower(self, s: str) -> int:
        prev = ""
        longest = 1
        
        for char in s:
            if not prev or prev[-1] == char:
                prev += char
            else:
                longest = max(longest, len(prev))
                prev = f"{char}"
        
        longest = max(longest, len(prev))
        return longest
    