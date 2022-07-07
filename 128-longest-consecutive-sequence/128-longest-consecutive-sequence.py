class Solution:
    def longestConsecutive(self, nums: list[int]):
        longest = 0
        num_set = set(nums)
        
        for val in num_set:
            if val - 1 not in num_set:
                curr = val
                curr_streak = 1
                
                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1
                    
                longest = max(longest, curr_streak)
                
        return longest
    