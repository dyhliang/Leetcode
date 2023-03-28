import numpy as np


class Solution:

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        l = 0
        ans = 0

        for r, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[l]
                l += 1

            ans += (r - l + 1)

        return ans
    