class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        occ = defaultdict(int)
        
        for c in arr:
            occ[c] += 1
        
        count = 0
        for key in occ.keys():
            if occ[key] == 1:
                count += 1
                
            if count == k:
                return key
            
        return ""