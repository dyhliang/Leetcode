class Solution:
    
    def rev_append(self, li):
        res = ""
        for pos in range(len(li)):
            if li[pos] == "0" and (pos == len(li) - 1):
                res += ""
            else:
                res += li[pos]
            
        return res
    
    def reverse(self, x: int) -> int:

        new_num = ""
        if x == 0:
            return 0
        elif x >= 1:
            list_num = [digit for digit in str(x)]
            list_num.reverse()
            
            new_num = self.rev_append(list_num)
            
            if int(new_num) > (2 ** 31 - 1):
                return 0
            else:
                return int(new_num)
        else:
            str_x = str(x)
            list_num = [str_x[pos] for pos in range(1, len(str_x))]
            list_num.reverse()
            
            new_num = self.rev_append(list_num)
            
            if int(new_num) * -1 < (-2 ** 31):
                return 0
            else:
                return int(new_num) * -1
            
