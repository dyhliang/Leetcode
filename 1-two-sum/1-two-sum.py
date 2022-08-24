class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        for pos, n in enumerate(nums):
            # We already know what the target is, so subtraction gets the other number
            diff = target - n
            if diff in prev:
                return [prev[diff], pos]
            
            prev[n] = pos
            # store the index as the value to the key of the other number