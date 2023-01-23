class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # We can't given a definitive answer unless at least all but 
        # 1 person responds
        if len(trust) < n - 1:
            return -1

        table = [0] * (n + 1)
        for arr in trust:
            table[arr[0]] -= 1
            table[arr[1]] += 1

        for i, val in enumerate(table[1:], 1):
            if val == n - 1:
                return i

        return -1