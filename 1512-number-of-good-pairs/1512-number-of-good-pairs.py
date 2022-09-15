import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        for pos, val in enumerate(nums):
            if val not in hashmap.keys():
                hashmap[val] = [pos]
            else:
                hashmap[val].append(pos)
        
        pairs = 0
        for key in hashmap.keys():
            l = len(hashmap[key])
            if l > 1:
                pairs += math.factorial(l)/(math.factorial(2) * math.factorial(l - 2))
                
        return int(pairs)