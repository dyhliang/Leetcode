class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums.sort()
        # This strategy only works if the array is sorted
        # Take the subarray from index 1 onwards, find its sum
        # Use that sum to subtract (the value at index 0 x the length of that subarray)
        total = sum(nums[1:])
        res = total - (nums[0] * len(nums[1:]))
        return res
    