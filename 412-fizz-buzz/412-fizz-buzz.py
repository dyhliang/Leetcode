class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            res.append(((i % 3 == 0)*"Fizz" + (i % 5 == 0)*"Buzz" or str(i)))
                       
        return res
    