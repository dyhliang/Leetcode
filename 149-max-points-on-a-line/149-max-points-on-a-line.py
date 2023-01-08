class Solution:
    def findSlope(self, p1, p2) -> float:
        if p1[0] != p2[0]:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        else:
            return float('inf')

    def maxPoints(self, points: list[list[int]]) -> int:
        res = 1

        if len(points) == 1:
            return res

        for i in range(len(points)):
            occ = Counter()
            max_occ = 1

            for j in range(i + 1, len(points)):
                slope = self.findSlope(points[i], points[j])
                occ[slope] += 1
                max_occ = max(occ[slope] + 1, max_occ)

            res = max(max_occ, res)

        return res
        