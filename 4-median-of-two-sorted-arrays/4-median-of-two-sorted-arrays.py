class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = nums1 + nums2
        merged_arr.sort()
        
        if len(merged_arr) % 2 == 0:
            return (merged_arr[int(len(merged_arr) / 2) - 1] + merged_arr[int(len(merged_arr) / 2)]) / 2
        else:
            return (merged_arr[len(merged_arr) // 2])
        