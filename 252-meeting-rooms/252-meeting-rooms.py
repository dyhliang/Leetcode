class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) == 0:
            return True
        
        intervals.sort()
        minheap = []
        heapq.heappush(minheap, intervals[0][1])
        
        for rng in intervals[1:]:
            if rng[0] >= minheap[0]:
                heapq.heappop(minheap)

            heapq.heappush(minheap, rng[1])


        return len(minheap) == 1
    