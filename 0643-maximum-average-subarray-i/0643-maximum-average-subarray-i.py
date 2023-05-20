class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        rsum = 0
        l, r = 0, 0
        max_avg = -float('inf')
        
        for n in nums:
            rsum += n
            window_len = r - l + 1
            curr_avg = rsum / window_len
            
            if window_len == k:
                max_avg = max(max_avg, curr_avg)
                rsum -= nums[l]
                l += 1

            r += 1
                
        return max_avg