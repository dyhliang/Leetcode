class Solution:
    def matrixReshape(self, mat, r, c):
        res = []
        comb_lst = []
        for lst in mat:
            comb_lst += lst
        
        # pos: pos+c partitions each block from the comb_lst
        if r * c == len(comb_lst):
            for pos in range(0,len(comb_lst), c):
                res.append(comb_lst[pos:pos+c])
        else:
            res = mat
        
        return res
    