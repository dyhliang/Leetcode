class Solution:
    def check(self, nums: list[int]) -> bool:
        s_nums = sorted(nums)
        if len(nums) == 1:
            return True
        elif nums == s_nums:
            return True

        biggest = max(nums)
        smallest = min(nums)
        highs = []
        lows = []

        for i, x in enumerate(nums):
            if x == biggest:
                highs.append(i)

            if x == smallest:
                lows.append(i)

        for n in highs:
            if n + 1 in lows:
                right = nums[0:n + 1]
                left = nums[n + 1:]
                combined = left + right
                sorted_nums = sorted(nums)
                return combined == sorted_nums

        return False
    