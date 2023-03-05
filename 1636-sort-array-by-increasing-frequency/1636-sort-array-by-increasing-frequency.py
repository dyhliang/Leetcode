class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        table = defaultdict(list)
        count = Counter(nums)
        res = []
        
        for c, v in count.items():
            table[v].append(c)
            
        sorted_table = sorted(table)
        for val in sorted_table:
            curr = sorted(table[val], reverse=True)
            for n in curr:
                res = res + [n] * val
                
        return res        
    