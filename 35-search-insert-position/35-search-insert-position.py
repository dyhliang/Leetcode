class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        # Use Binary Search to look for the index as the array is already sorted.
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
            
        # Instead of returning -1 if not found, left would be where the last pointer goes
        # given that nums[left] is the smallest number less than the target.
        return left
    