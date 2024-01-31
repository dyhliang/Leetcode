class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][0]:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                    
                stack.append((temp, i))
                    
        return res