class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        rightsum = [sum(nums[1:])]
        
        for n in nums[:-1]:
            leftsum.append(leftsum[-1] + n)
            
        for n in nums[1:]:
            rightsum.append(rightsum[-1] - n)
            
        diff = [abs(rightsum[i] - leftsum[i]) for i in range(0, len(leftsum))]
        
        return diff
        