class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        # Use Binary Search to look for the index as the array is already sorted.
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
            
        return left
    