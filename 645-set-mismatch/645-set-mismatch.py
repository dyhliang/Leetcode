from collections import OrderedDict

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        seen = [0] * (max(nums) + 2)
        res = []
        for val in nums:
            seen[val] += 1

            if seen[val] == 2:
                res.append(val)

        for n in range(1, nums[-1] + 1):
            if seen[n] == 0:
                res.append(n)
                break

        if len(res) == 1:
            res.append(nums[-1] + 1)

        return res
