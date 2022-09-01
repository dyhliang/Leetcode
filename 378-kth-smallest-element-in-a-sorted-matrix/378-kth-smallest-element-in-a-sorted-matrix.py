import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_rows = []
        for arr in matrix:
            all_rows += arr
            
        min_heap = []
        for val in all_rows:
            heapq.heappush(min_heap, val)
            
        while k > 0:
            val = heapq.heappop(min_heap)
            k -= 1
        
        return val
    