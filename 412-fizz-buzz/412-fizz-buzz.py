class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fizz_map = {3: "Fizz", 5: "Buzz"}
        
        for i in range(1, n+1):
            s = ""
            for key in fizz_map.keys():
                if i % key == 0:
                    s += fizz_map[key]
                    
            if s == "":
                s += str(i)
            
            res.append(s)
                
        return res
    