class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        seen_maxes = []
        curr_max = -float('inf')

        for val in reversed(arr):
            if val >= curr_max:
                curr_max = val
                seen_maxes.append(val)

        j = len(seen_maxes) - 1
        for i, val in enumerate(arr):
            if arr[i] >= seen_maxes[j] and j > 0:
                j -= 1

            arr[i] = seen_maxes[j]

        arr[-1] = -1
        return arr

    