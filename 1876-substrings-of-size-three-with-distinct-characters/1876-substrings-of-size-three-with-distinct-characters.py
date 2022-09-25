from collections import deque

class Solution:
    def countGoodSubstrings(self, s: str) -> int:     
        
        window = deque([])
        count = 0

        for i, char in enumerate(s):
            if len(window) > 0:
                if window[-1] == char:
                    window = deque([])
            
            if len(window) > 2:
                window.popleft()
                
            if char not in window and len(window) == 2:
                count += 1
                
            window.append(char)
        
        return count
    