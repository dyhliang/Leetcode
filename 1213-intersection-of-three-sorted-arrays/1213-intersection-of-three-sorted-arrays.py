class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr_intersection = [val for val in arr1 if val in arr2 and val in arr3]
        res = list(set(arr_intersection))
        res.sort()
        return res
        