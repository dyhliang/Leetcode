class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: 

        if len(intervals) == 0:
            return 0
        
        intervals.sort()
        minheap = []
        heapq.heappush(minheap, intervals[0][1])
        
        for rng in intervals[1:]:
            if rng[0] >= minheap[0]:
                heapq.heappop(minheap)

            heapq.heappush(minheap, rng[1])


        return len(minheap)