class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = deque([])
        indices = deque([])
        res = []
        p_ana = "".join(sorted([*p]))
        
        for i, char in enumerate(s):
            window.append(char)
            indices.append(i)
            if len(window) == len(p):
                ana = "".join(sorted(window))
                if ana == p_ana:
                    res.append(indices[0])
                    
                indices.popleft()
                window.popleft()

        return res
    