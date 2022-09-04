class Solution:
    def diagonalSum(self, arr: list[list[int]]) -> int:
        left = 0
        right = len(arr[0]) - 1
        total = 0

        for i in range(len(arr)):

            if i == (len(arr) - i - 1):
                total += arr[i][i]
            else:
                if i == left:
                    total += arr[i][i]

                if (len(arr) - i - 1) == right:
                    total += arr[i][len(arr) - i - 1]

            left += 1
            right -= 1


        return total
