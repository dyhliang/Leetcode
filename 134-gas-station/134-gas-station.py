class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff_list = [gas[x] - cost[x] for x in range(len(cost))]
        total = 0
        start = 0
        
        for i, val in enumerate(diff_list):
            total += val
            
            if total < 0:
                total = 0
                start = i + 1
                
        return start

        