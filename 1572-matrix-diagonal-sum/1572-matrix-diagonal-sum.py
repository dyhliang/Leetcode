class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left = 0
        right = len(mat[0]) - 1
        total = 0
        
        for arr in mat:
            for i in range(len(arr)):
                
                if i == left == right:
                    total += arr[i]
                else:
                    if i == left:
                        total += arr[i]

                    if i == right:
                        total += arr[i]

            left += 1
            right -= 1
        
        return total
    