import random

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.backup = []
        for val in nums:
            self.backup.append(val)

    def reset(self) -> list[int]:
        return self.backup

    def shuffle(self) -> list[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()