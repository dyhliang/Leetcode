class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Use Gauss's Formula to get the sum of all numbers up to n, including the missing one, then subtract the sum of the current nums list to find the missing num.
        total = len(nums)
        gauss_sum = (total * (total + 1)) // 2
        curr_sum = sum(nums)
        return gauss_sum - curr_sum
    