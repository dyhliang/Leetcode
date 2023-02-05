class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = deque([])
        res = []
        p_ana = "".join(sorted([*p]))
        
        for i, char in enumerate(s):
            window.append(char)

            if len(window) == len(p):
                ana = "".join(sorted(window))
                if ana == p_ana:
                    res.append(i - (len(p) - 1))
                    
                window.popleft()

        return res
    