class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        streak = 0
        max_streak = 0
        
        for num in arr:
            if streak > 0:
                if num % 2 == 0:
                    streak = 0
                else:
                    streak += 1
                    max_streak = max(max_streak, streak)
            else:
                if num % 2 == 1:
                    streak = 1
        
        return max_streak >= 3
    