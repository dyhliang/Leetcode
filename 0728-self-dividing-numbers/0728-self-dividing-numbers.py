class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for val in range(left, right+1):
            digits = [*(str(val))]
            if '0' not in digits:
                res.append(val)
                
                for d in digits:
                    if res and val % int(d) != 0:
                        res.pop()
                        break
                    
        return res
    