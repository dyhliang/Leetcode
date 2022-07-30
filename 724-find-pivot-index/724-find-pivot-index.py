class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        left_sum = 0
        arr_sum = sum(arr)
        
        for index, val in enumerate(arr):
            if left_sum == (arr_sum - left_sum - val):
                return index
            
            left_sum += val
        
        return -1
    