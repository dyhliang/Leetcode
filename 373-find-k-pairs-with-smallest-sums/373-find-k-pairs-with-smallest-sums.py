import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxheap = [] 
        # Still functions like a minheap, but we'll use the sign visual trick to modify every value to its opposite sign so technically heappop still pops the smallest value
        
        for p1 in range(0, min(k, len(nums1))):
            for p2 in range(0, min(k, len(nums2))):
                total = nums1[p1] + nums2[p2]
                
                if len(maxheap) < k:
                    heapq.heappush(maxheap, [-total, nums1[p1], nums2[p2]])
                else:
                    # If the sum is larger than the 'largest' sum on the heap, we can break as it would be impossible to find a smaller pair sum given that the array is sorted in ascending order.
                    if total > -maxheap[0][0]:
                        break
                
                    heapq.heappush(maxheap, [-total, nums1[p1], nums2[p2]])
                    heapq.heappop(maxheap)

        res = []
        while maxheap:
            pair = heapq.heappop(maxheap)
            res.append([pair[1], pair[2]])

        return res
    