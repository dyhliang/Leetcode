class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        total = 0
        for val in nums:
            total += val
            res.append(total)
            
        return res
    