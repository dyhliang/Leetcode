class Solution:
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        digits_raised = [int(d) ** len(str_n) for d in str_n]
        return sum(digits_raised) == n
                          