import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minheap = []
        
        for i in range(len(mat)):
            s = sum(mat[i])
            heapq.heappush(minheap, (s, i))
        
        res = []
        while k > 0:
            val = heapq.heappop(minheap)
            res.append(val[1])
            k -= 1
            
        return res
            