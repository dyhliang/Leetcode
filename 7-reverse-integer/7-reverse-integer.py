class Solution:
    def reverse(self, x: int) -> int:
        if x in range(-9, 10):
            return x
        
        new_num = ""
        if x >= 10:
            list_num = [digit for digit in str(x)]
            list_num.reverse()
            
            for pos in range(len(list_num)):
                if list_num[pos] == "0" and (pos == 0 or pos == len(list_num) - 1):
                    new_num += ""
                else:
                    new_num += list_num[pos]
            
            if int(new_num) > (2 ** 31 - 1):
                return 0
            else:
                return int(new_num)
        else:
            str_x = str(x)
            list_num = [str_x[pos] for pos in range(1, len(str_x))]
            list_num.reverse()
            
            for pos in range(0, len(list_num)):
                if list_num[pos] == "0" and (pos == 0 or pos == len(list_num) - 1):
                    new_num += ""
                else:
                    new_num += list_num[pos]
              
            if int(new_num) * -1 < -2147483648:
                return 0
            else:
                return int(new_num) * -1
            
