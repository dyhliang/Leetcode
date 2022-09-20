class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1:
            # Use list comp. to compute the sums of each digit squared
            n = sum([int(x) ** 2 for x in str(n)])
            
            # Use seen to store values that have already been generated, if we come across
            # that value again, there's no point in revisitng that number, so break out
            if n not in seen:
                seen.add(n)
            else:
                break
            
        # If n never gets to one, it will evaluate to False, True otherwise
        return n == 1
    