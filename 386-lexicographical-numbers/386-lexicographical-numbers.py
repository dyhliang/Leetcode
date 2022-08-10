class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n+1)]
        res.sort()
        return res
            