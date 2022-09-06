class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in seen.keys():
                seen[n] = i
            else:
                res = [seen[target-n], i]
                
        return res
