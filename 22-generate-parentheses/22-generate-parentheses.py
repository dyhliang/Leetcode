class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(stack=[], left=0, right=0):
            if len(stack) == n * 2:
                res.append("".join(stack))
                return
            else:
                if left < n:
                    stack.append("(")
                    backtrack(stack, left+1, right)
                    stack.pop()
                if right < left:
                    stack.append(")")
                    backtrack(stack, left, right+1)
                    stack.pop()
                    
        backtrack()
        return res