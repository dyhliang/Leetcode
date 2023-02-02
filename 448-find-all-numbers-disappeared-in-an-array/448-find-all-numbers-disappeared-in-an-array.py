class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        table = [0] * max((max(set(nums)) + 1), len(nums) + 1)
        res = []

        for val in nums:
            table[val] += 1

        for i in range(1, len(table)):
            if table[i] == 0:
                res.append(i)

        return res