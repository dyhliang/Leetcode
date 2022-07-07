class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fizz_map = {3: "Fizz", 5: "Buzz"}
        
        for i in range(1, n+1):
            s = ""      # resets the string for every iteration from 1 to n
            for key in fizz_map.keys():
                if i % key == 0:
                    s += fizz_map[key]  # Won't need to check for divisiblity by 15
                    
            if s == "": # If number is not divisible by 3 or 5, s will be empty
                s += str(i)
            
            res.append(s)
                
        return res
    