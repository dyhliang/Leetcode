class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_list = list(jewels)
        res = 0
        for item in jewels_list:
            res += stones.count(item)
            
        return res
    