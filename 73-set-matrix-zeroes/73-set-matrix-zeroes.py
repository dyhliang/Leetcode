class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Map the row and col coordinates where 0 is found 
        zero_loc = {"r": [],
                    "c": []}
        
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if matrix[i][j] == 0:
                    zero_loc["r"].append(i)
                    zero_loc["c"].append(j)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in zero_loc["r"] or j in zero_loc["c"]:
                    matrix[i][j] = 0

        return matrix
    