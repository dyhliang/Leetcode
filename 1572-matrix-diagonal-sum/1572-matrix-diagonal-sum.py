class Solution:
    def diagonalSum(self, arr: list[list[int]]) -> int:
        total = 0

        for i in range(len(arr)):

            if i == (len(arr) - i - 1):
                total += arr[i][i]
            else:
                total += (arr[i][i] + arr[i][len(arr) - i - 1])

        return total
