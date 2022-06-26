class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # assigns the coordinates of the entire matrix stored in one list into groupings
        box_groups = {
            1: [0, 1, 2, 9, 10, 11, 18, 19, 20],
            2: [3, 4, 5, 12, 13, 14, 21, 22, 23],
            3: [6, 7, 8, 15, 16, 17, 24, 25, 26],
            4: [27, 28, 29, 36, 37, 38, 45, 46, 47],
            5: [30, 31, 32, 39, 40, 41, 48, 49, 50],
            6: [33, 34, 35, 42, 43, 44, 51, 52, 53],
            7: [54, 55, 56, 63, 64, 65, 72, 73, 74],
            8: [57, 58, 59, 66, 67, 68, 75, 76, 77],
            9: [60, 61, 62, 69, 70, 71, 78, 79, 80],
            }
        
        comb = []
        for lst in board:
            comb += lst
            
        # stores occurrences of each value within each box into dict to check for duplicates
        for key in box_groups:
            box_occ = {}
            # index thru the list of each key inside box_groups
            for index in box_groups[key]:
                if comb[index] != ".":
                    box_occ[comb[index]] = 1 + box_occ.get(comb[index], 0)
                    
                if 2 in box_occ.values():
                    return False          

        # stores occurrences of each value within each row        
        for lst in board:
            row_occ = {}
            for ele in lst:
                if ele != ".":
                    row_occ[ele] = 1 + row_occ.get(ele, 0)
                    
                if 2 in row_occ.values():
                    return False
    
        # stores occurrences of each value within each column, row[0][0] to row[8][0], then row[0][1] to row[8][1], so on...
        col_pos = 0
        while col_pos < len(board):
            col_occ = {}
            row_pos = 0
            while row_pos < len(board):
                if board[row_pos][col_pos] != ".":
                    col_occ[board[row_pos][col_pos]] = 1 + col_occ.get(board[row_pos][col_pos], 0)
                    
                if 2 in col_occ.values():
                    return False
                row_pos += 1
            col_pos += 1

        return True
        