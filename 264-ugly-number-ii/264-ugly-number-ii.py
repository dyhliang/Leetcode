import heapq

class Solution:
    
    def isUgly(self, n: int, seen: set, h: list) -> bool:
        for p in [2, 3, 5]:
            new_ugly = n * p
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(h, new_ugly)
                
    
    def nthUglyNumber(self, n: int) -> int:
        
        seen = {1, }
        nums = []
        heap = []
        heapq.heappush(heap, 1)
        
        for val in range(1690):
            curr = heapq.heappop(heap)
            nums.append(curr)
            self.isUgly(curr, seen, heap)
            
        return nums[n-1]
