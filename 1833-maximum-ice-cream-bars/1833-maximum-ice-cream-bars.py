class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        total = 0
        count = 0
        
        for val in sorted_costs:
            if total + val > coins:
                return count
            else:
                total += val
                count += 1
        
        return count