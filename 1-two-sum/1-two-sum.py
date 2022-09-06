class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in seen.keys():
                seen[n] = i
            else:
                res = [seen[diff], i]
                return res
