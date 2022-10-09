from collections import deque

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = deque([])
        max_avg = sum(nums[0:k]) / k
        
        # Running sum() in the for loop results in TLE, have to keep track of running sum to get under it
        curr_avg = max_avg
        curr_sum = 0
        
        for val in nums:
            window.append(val)
            curr_sum += val
            
            if len(window) == k:
                curr_avg = curr_sum / k
                max_avg = max(curr_avg, max_avg)
                popped = window.popleft()
                curr_sum -= popped
        
        return max_avg
    