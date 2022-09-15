import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Use a hash table to map the index of each value to the val
        hashmap = {}
        for pos, val in enumerate(nums):
            if val not in hashmap.keys():
                hashmap[val] = [pos]
            else:
                hashmap[val].append(pos)
        
        # This is a combinations problem, where order doesn't matter based on Ex. 1 - (3, 0) is not mentioned with (0, 3)
        pairs = 0
        for key in hashmap.keys():
            n = len(hashmap[key])
            # Combinations are only possible if there's 2 or more numbers to work with
            if n > 1:
                # Use the combinations formula where n is the length of numbers in value arr
                # r is 2
                # n!/r!(n-r)!
                pairs += math.factorial(n)/(math.factorial(2) * math.factorial(n - 2))
                
        return int(pairs)
    