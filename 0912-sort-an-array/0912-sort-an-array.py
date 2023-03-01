class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        low = min(nums)
        if low > 0:
            low = 0

        high = max(nums)
        diff = high - low
        table = [0] * (diff + 1)
        res = []

        for val in nums:
            table[val - low] += 1

        for i, ct in enumerate(table):
            for c in range(ct):
                res.append(i + low)

        return res
    