from collections import deque

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        if sorted_nums[0] == sorted_nums[-1]:
            return 0
        
        d = deque([sorted_nums[0]])
        longest = 0
        
        for n in sorted_nums[1:]:
            if abs(n - d[-1]) in range(2) and abs(n - d[0]) in range(2):
                d.append(n)
            else:
                if len(d) > 1 and d[0] != d[-1]:
                    longest = max(longest, len(d))
                    while d and abs(n - d[0]) > 1:
                        d.popleft()
                else:
                    d = deque([])

                d.append(n)
        
        longest = max(longest, len(d))
        if longest == 1:
            return 0
        else:
            return longest