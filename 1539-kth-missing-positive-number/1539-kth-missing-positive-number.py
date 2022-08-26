class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high = max(arr)
        count = 0

        for val in range(1, high + 1):
            if val not in arr:
                count += 1
                if count == k:
                    return val

        if count < k:
            return high + (k - count)
        