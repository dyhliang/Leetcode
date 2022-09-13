class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        hasht = {3: "Fizz", 5: "Buzz"}
        res = []
        for i in range(1, n+1):
            string = ""
            for key in hasht.keys():
                if i % key == 0:
                    string += hasht[key]
            
            if string == "":
                string = str(i)

            res.append(string)
                       
        return res
    