class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()  # sorts the arr to get adjacent values to be 'closer' to each other
        min_diff = arr[1] - arr[0]
        diff_pairs = []

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < min_diff:
                min_diff = arr[i + 1] - arr[i]

            diff_pairs.append([arr[i], arr[i + 1]])

        # check back to see which pairs have a difference == min diff
        # Do this without second for loop?
        res = [pair for pair in diff_pairs if pair[1] - pair[0] == min_diff]

        return res
    