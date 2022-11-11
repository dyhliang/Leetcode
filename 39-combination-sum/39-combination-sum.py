from copy import deepcopy

class Solution:

    def backtrack(self, nums, start, result, remainder, combination):
        if remainder == 0:
            result.append(deepcopy(combination))
            return
        elif remainder < 0:
            return  # sum exceeded the target
        for i in range(start, len(nums)):
            combination.append(nums[i])
            self.backtrack(nums, i, result, remainder - nums[i], combination)
            # backtrack
            combination.pop()
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        self.backtrack(candidates, 0, result, target, [])
        return result
    