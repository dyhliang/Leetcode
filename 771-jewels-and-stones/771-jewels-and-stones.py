class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_list = list(jewels)
        res = 0
        hash_t = {}
        
        for ele in stones:
            hash_t[ele] = 1 + hash_t.get(ele, 0)
        
        for item in jewels_list:
            if item in stones:
                res += hash_t[item]
            
        return res
    