class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_table = defaultdict(int)
        col_table = defaultdict(int)
        curr_row = []
        curr_col = []
        ans = 0
        
        for r in grid:
            for c in r:
                curr_row.append(str(c) + ",")
            curr_row_str = "".join(curr_row)
            row_table[curr_row_str] += 1
            curr_row = []
            
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                curr_col.append(str(grid[j][i]) + ",")
            curr_col_str = "".join(curr_col)
            col_table[curr_col_str] += 1
            curr_col = []
            
        for k in row_table.keys():
            if col_table[k] >= 1:
                ans += (row_table[k] * col_table[k])
                
        return ans
            