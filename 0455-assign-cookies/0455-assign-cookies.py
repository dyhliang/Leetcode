class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)[::-1]
        s = sorted(s)[::-1]
        g_len = len(g)
        s_len = len(s)
        gi, si = 0, 0
        ans = 0
        
        while gi < g_len and si < s_len:
            if s[si] >= g[gi]:
                gi += 1
                si += 1
                ans += 1
            else:
                gi += 1
                
        return ans
        