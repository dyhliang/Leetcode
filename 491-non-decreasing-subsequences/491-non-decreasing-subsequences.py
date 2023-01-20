class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, combo = [], []

        def backtrack(i: int) -> None:
            n = len(nums)
            if i == n:
                if len(combo) > 1 and combo not in res:
                    dcopy = copy.deepcopy(combo)
                    res.append(dcopy)
                return

            if not combo or nums[i] >= combo[-1]:
                combo.append(nums[i])
                backtrack(i + 1)
                combo.pop()

            backtrack(i + 1)

        backtrack(0)
        return res