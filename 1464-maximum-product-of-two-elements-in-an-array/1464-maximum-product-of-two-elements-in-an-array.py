import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxheap = []
        for val in nums:
            heapq.heappush(maxheap, -val)
            
        num1 = heapq.heappop(maxheap)
        num2 = heapq.heappop(maxheap)
        
        return (-num1-1) * (-num2-1)
    