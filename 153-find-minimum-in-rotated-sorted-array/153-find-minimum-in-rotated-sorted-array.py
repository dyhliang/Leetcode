class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #if len(nums) == 2:
        #    return min(nums[0], nums[1])
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = (left + right) // 2
            
            if middle != 0 and nums[middle - 1] > nums[middle]:
                return nums[middle]
            elif nums[middle] > nums[middle+1]:
                return nums[middle+1]
            else:
                if nums[left] < nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1

        return nums[0]
    