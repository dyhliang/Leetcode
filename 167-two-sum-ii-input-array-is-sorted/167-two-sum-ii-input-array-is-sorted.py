class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            total = nums[low] + nums[high]
            
            if total == target:
                return [low+1, high+1]
            elif total < target:
                low += 1
            else:
                high -= 1
                
        return [-1, -1]
    