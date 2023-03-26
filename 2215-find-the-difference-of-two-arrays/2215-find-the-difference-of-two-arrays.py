class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        new_nums1 = []
        new_nums2 = []
        for i, val in enumerate(nums1):          
            table1[val] += 1
            
        for i, val in enumerate(nums2):
            table2[val] += 1
            
        for k in table1.keys():
            if k not in table2.keys():
                new_nums1.append(k)
                
        for k in table2.keys():
            if k not in table1.keys():
                new_nums2.append(k)
        
        return [new_nums1, new_nums2]
    