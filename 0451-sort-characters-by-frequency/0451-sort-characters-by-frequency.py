import heapq as hq

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        
        for c in s:
            dic[c] += 1
            
        res = ""
        occ = []
        
        for key in dic:
            occ.append([dic[key], key])
        
        occ.sort()
        
        for val in reversed(occ):
            char_occ = val[0]
            char = val[1]
            res += (char_occ * char)
        
        return res
            