import copy
from collections import defaultdict


class Solution:
    def backtrack(self, combo, res, target, candidates, table, seen):
        if sum(combo) == target:
            combo_copy = copy.deepcopy(combo)
            table_copy = copy.deepcopy(table)
            if table_copy not in seen:
                res.append(combo_copy)
                seen.append(table_copy)
            return
        elif sum(combo) > target:
            return

        for val in candidates:
            combo.append(val)
            table[val] += 1
            self.backtrack(combo, res, target, candidates, table, seen)
            popped = combo.pop()
            table[popped] -= 1
            if table[popped] == 0:   # deletes the entry in the dict if its occ goes to 0
                table.pop(popped)

    def combinationSum(self, candidates: list[int], target: int):
        res = []
        self.backtrack([], res, target, candidates, defaultdict(int), [])
        return res
    