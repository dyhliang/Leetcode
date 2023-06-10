class Solution:
    def countElements(self, arr: List[int]) -> int:
        maxnum = max(arr)
        occ = [0] * (maxnum + 1)
        
        for n in arr:
            occ[n] = 1
            
        count = 0
        for n in arr:
            if n != maxnum:
                count += occ[n + 1]
            
        return count
            