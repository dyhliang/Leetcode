class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_ends = [[p[1], p[0]] for p in points]
        points_ends.sort()
        count = 1
        first_end = points_ends[0][0]

        for p in points_ends:
            if first_end < p[1]:
                count += 1
                first_end = p[0]

        return count
    