class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr_intersection = [val for val in nums1 if val in nums2]
        
        return list(set(arr_intersection))