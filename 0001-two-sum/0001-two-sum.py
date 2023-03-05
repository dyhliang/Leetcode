class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, val in enumerate(nums):
            if val not in table.keys():
                diff = target - val
                table[diff] = i
            else:
                return [table[val], i]