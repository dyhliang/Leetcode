class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        table = {
            3: "Fizz",
            5: "Buzz"
        }
        
        res = []
        for val in range(1, n+1):
            ans = ""
            for div in table.keys():
                if val % div == 0:
                    ans += table[div]
            
            if ans == "":
                ans = str(val)
                
            res.append(ans)
            
        return res
    