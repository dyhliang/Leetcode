class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        window = []
        longest = 1
        
        for n in nums:
            if not window or n > window[-1]:
                window.append(n)
            else:
                longest = max(len(window), longest)
                window = [n]
              
        longest = max(len(window), longest)
        return longest
            