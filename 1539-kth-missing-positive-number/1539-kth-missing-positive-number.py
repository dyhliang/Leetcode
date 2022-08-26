class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high = max(arr)
        occ = {}
        count = 0
        for val in range(1, high + 1):
            if val in arr:
                occ[val] = 1 + occ.get(val, 0)
            else:
                occ[val] = 0
                count += 1
                if count == k:
                    return val

        if list(occ.values()).count(0) < k:
            return high + (k - count)
        