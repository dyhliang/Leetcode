class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        hasht = {3: "Fizz", 5: "Buzz"}
        res = []
        for i in range(1, n+1):
            string = ""
            for key in hasht.keys():
                # Reduces the need for multiple ifs to test 3, 5, and 15
                if i % key == 0:
                    string += hasht[key]
            
            # If the string wasn't modified, then i is not divisible by 3, 5, and 15
            if string == "":
                string = str(i)

            res.append(string)
                       
        return res
    