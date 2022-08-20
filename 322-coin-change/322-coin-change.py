class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Iterate from last pos in array, keep checking that adding curr position to total            is less than amount  until it is > amount, then move back a space, repeat

        If total == amount at any point, return

        If we get to the end of the list and the total =/= amount, return -1
        """
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    arr[i] = min(arr[i], 1 + arr[i - coins[j]])
                
        
        if arr[amount] > amount:
            return -1
        else:
            return arr[amount]
        