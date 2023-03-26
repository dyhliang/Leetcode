class Solution:
    def updateTable(self, arr, table):
        for n in arr:
            table[n] == 1
            
    def updateNewArr(self, new_arr, ta, tb):
        for k in ta.keys():
            if k not in tb.keys():
                new_arr.append(k)
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1, table2 = defaultdict(int), defaultdict(int)
        new_nums1, new_nums2 = [], []
        self.updateTable(nums1, table1)
        self.updateTable(nums2, table2)
        
        self.updateNewArr(new_nums1, table1, table2)
        self.updateNewArr(new_nums2, table2, table1)
        return [new_nums1, new_nums2]
    