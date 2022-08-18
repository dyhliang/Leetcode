class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        new_nums = set(nums)
        res = [val for val in new_nums if nums.count(val) > (len(nums) // 3)]
        return set(res)
    