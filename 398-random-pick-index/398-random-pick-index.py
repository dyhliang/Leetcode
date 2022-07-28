import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.occs = {}  # Store positions of each number into list within a hashmap
        
        for pos in range(len(nums)):
            if nums[pos] not in self.occs.keys():
                self.occs[nums[pos]] = [pos]
            else:
                self.occs[nums[pos]].append(pos)

    def pick(self, target: int) -> int:
        return random.choice(self.occs[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)