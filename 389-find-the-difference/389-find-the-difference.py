class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [*s]
        t_list = [*t]
        s_list.sort()
        t_list.sort()

        
        for pos in range(max(len(s_list), len(t_list))):
            if pos >= len(s_list):
                return t_list[pos]
            
            if s_list[pos] != t_list[pos]:
                return t_list[pos]
            