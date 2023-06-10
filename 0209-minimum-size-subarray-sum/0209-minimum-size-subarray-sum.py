class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = len(nums)
        window = deque([nums[0]])
        window_sum = nums[0]
        i = 1
        
        while window:
            if window_sum >= target:
                minlen = min(minlen, len(window))
                
                while window_sum >= target:
                    val = window.popleft()
                    window_sum -= val
                    if window_sum >= target:
                        minlen = min(minlen, len(window))
            else:
                if i == len(nums):
                    break
                else:
                    window.append(nums[i])
                    window_sum += nums[i]
                    i += 1
                    
        if window_sum < target and len(window) == len(nums):
            return 0
        else:
            return minlen
        # [2,5,6,8,12,15]
    