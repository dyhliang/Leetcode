class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # We don't care about which element was distinct or not,
        # so simply strip out duplicates in nums with set() and then
        # compare with the length of the original
        return len(set(nums)) != len(nums)