class Solution:
    
    def backtrack(self, res, digits, i, combo):
        
        table = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(combo) == len(digits):
            choice = "".join(copy.deepcopy(combo))
            res.append(choice)
            return

        group = table[digits[i]]
        for letter in group:
            combo.append(letter)
            self.backtrack(res, digits, i+1, combo)
            combo.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        if len(digits) == 0:
            return res
        else:
            self.backtrack(res, digits, 0, [])
            return res
    