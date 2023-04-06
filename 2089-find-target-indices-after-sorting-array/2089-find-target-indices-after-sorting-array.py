class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        res = [i for i, val in enumerate(sorted_nums) if val == target]
        return res
    