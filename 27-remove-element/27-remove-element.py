class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        for i, n in enumerate(nums):
            if n == val:
                if i == len(nums) - 1:
                    nums[i] = "_"
                    return i

                while nums[i] == nums[end] and end > 0:
                    nums[end] = "_"
                    end -= 1

                if nums[i] == "_":
                    return i
                else:
                    nums[i] = nums[end]
                    nums[end] = "_"
                    end -= 1

            if nums[i] == "_" or end < 0:
                return i