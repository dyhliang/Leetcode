class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for r in matrix:
            row_seen = set()
            for c in r:
                row_seen.add(c)
            
            if len(row_seen) != len(r):
                return False
            
        for c, col in enumerate(matrix):
            col_seen = set()
            for r, n in enumerate(col):
                col_seen.add(matrix[r][c])
                
            if len(col_seen) != len(matrix[0]):
                return False
            
        return True
    