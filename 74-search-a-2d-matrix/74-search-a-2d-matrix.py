class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        comb_m = []
        for inner_m in matrix:
            comb_m += inner_m
        
        left = 0
        right = len(comb_m) - 1
        while left <= right:
            middle = (left + right) // 2
            
            if comb_m[middle] == target:
                return True
            elif comb_m[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
            