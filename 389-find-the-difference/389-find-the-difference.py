class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sort = sorted(s)
        t_sort = sorted(t)
        
        # Sort the letters inside the two strings
        # If the pointer gets past the last position of s, return the value at that pos in t, this if statement goes first so the ensuing if statement won't get an out of bounds error comparing a character at a position that doesn't exist.
        for pos in range(max(len(s), len(t))):
            if pos >= len(s_sort):
                return t_sort[pos]
            
            if s_sort[pos] != t_sort[pos]:
                return t_sort[pos]
            