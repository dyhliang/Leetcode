class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groupings = {}
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groupings:
                    groupings[r-c] = val
                elif groupings[r-c] != val:
                    return False
        
        return True
        