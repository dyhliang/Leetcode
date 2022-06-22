class Solution:
    def generate(self, numRows: int):
        r = 1
        index = 1
        res = []
        while r <= numRows:
            new_list = [0] * r
            new_list[0] = 1
            new_list[r-1] = 1
            index = 1
            while index < r-1:
                new_list[index] = res[r-2][index-1] + res[r-2][index]
                index += 1
            
            res.append(new_list)
            r += 1
        
        return res
    