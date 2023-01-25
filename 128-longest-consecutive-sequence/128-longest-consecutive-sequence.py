class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        numset = set(nums)
        
        for num in numset:
            if num - 1 not in numset:
                curr = num
                streak = 1
                
                while curr + 1 in numset:
                    curr += 1
                    streak += 1
                    
                longest_streak = max(longest_streak, streak)
        
        return longest_streak