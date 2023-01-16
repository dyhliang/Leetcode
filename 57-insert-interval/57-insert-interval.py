class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        overlaps, res = [], []
        local_min, local_max = float('inf'), -float('inf')
        newIntervalRange = range(newInterval[0], newInterval[1] + 1)

        for pair in intervals:
            pair_range = range(pair[0], pair[1]+1)
            if pair[0] in newIntervalRange or pair[1] in newIntervalRange or newInterval[0] in pair_range or newInterval[1] in pair_range:
                overlaps.append(pair)
                local_min = min(pair[0], newInterval[0], local_min)
                local_max = max(pair[1], newInterval[1], local_max)

        new_int = [local_min, local_max]

        for p in intervals:
            if len(overlaps) == 0:
                if newInterval[0] < p[0]:
                    res.append(newInterval)
                    res.append(p)
                else:
                    res.append(p)
                    res.append(newInterval)

                # Workaround so the above if condition stops being true
                overlaps.append(new_int)
            else:
                if p not in overlaps:
                    res.append(p)
                elif p == overlaps[0]:
                    res.append(new_int)

        res.sort()
        return res