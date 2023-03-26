class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        new_nums1 = set()
        new_nums2 = set()
        for i, val in enumerate(nums1):          
            table1[val] += 1
            
        for i, val in enumerate(nums2):
            table2[val] += 1
            
        for i, val in enumerate(nums1):
            if val not in table2.keys():
                new_nums1.add(val)
                
        for i, val in enumerate(nums2):
            if val not in table1.keys():
                new_nums2.add(val)
        
        return [list(new_nums1), list(new_nums2)]
    