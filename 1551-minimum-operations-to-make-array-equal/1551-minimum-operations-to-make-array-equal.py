class Solution:
    def minOperations(self, n: int) -> int:
        # n = 1: 0 [1]
        # n = 2: 1 [1, 3]
        # n = 3: 2 [1, 3, 5]
        # n = 4: 4 [1, 3, 5, 7]
        # n = 5: 6 [1, 3, 5, 7, 9]
        # n = 6: 9 [1, 3, 5, 7, 9, 11]
        # n = 7: 12 [1, 3, 5, 7, 9, 11, 13]
        # n = 10: 25 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        if n % 2 == 0:
            new_n = n ** 2
        else:
            new_n = n ** 2 - 1
        
        return new_n // 4
    