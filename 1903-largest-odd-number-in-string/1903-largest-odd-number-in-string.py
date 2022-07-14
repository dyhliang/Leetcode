class Solution:
    def largestOddNumber(self, num: str) -> str:

        res = ""
        if int(num) % 2 == 1:
            res = num
            return res
        else:
            for i in range(len(num)-1, -1, -1):
                if int(num[i]) % 2 == 1:
                    res = num[0:i+1]
                    return res

            
            return res
            