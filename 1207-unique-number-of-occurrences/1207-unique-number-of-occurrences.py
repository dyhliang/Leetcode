class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for val in arr:
            d[val] = 1 + d.get(val, 0)
            
        return len(d.values()) == len(set(d.values()))
            