class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indices = []
        res = [0] * len(s)
        for i, char in enumerate(s):
            if char == c:
                c_indices.append(i)
                
        if len(c_indices) >= 2:
            j = 1
        else:
            j = 0
            
        for i, char in enumerate(s):
            if char != c:
                res[i] = min(abs(i - c_indices[j]), abs(i - c_indices[j-1]))
                
            if i == c_indices[j] and j < len(c_indices) - 1:
                j += 1
            
        return res
    