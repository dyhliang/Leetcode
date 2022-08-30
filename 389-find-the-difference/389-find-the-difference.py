class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [*s]
        t_list = [*t]
        s_list.sort()
        t_list.sort()
        
        # Sort the letters inside the two strings
        # If the pointer gets past the last position of s, return the value at that pos in t, this if statement goes first so the ensuing if statement won't get an out of bounds error comparing a character at a position that doesn't exist.
        for pos in range(max(len(s_list), len(t_list))):
            if pos >= len(s_list):
                return t_list[pos]
            
            if s_list[pos] != t_list[pos]:
                return t_list[pos]
            