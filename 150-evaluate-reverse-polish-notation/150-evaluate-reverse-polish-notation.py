class Solution:

    def add(self, n1, n2) -> int:
        return n1 + n2

    def subtract(self, n1, n2) -> int:
        return n1 - n2

    def multiply(self, n1, n2) -> int:
        return n1 * n2

    def divide(self, n1, n2) -> int:
        if n1 / n2 < 0:
            return math.ceil(n1 / n2)
        else:
            return n1 // n2

    def evalRPN(self, tokens: list[str]) -> int:
        # Plan: Use a stack, pop top 2 numbers off as we encounter operations
        # The value evaluated from 2 numbers and operations goes back on the stack
        # Keep doing this until we reach end of tokens, then return value from stack

        stack = []
        operators = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

        for s in tokens:
            if s not in operators.keys():
                stack.append(int(s))
            elif len(stack) >= 2:
                n2 = stack.pop()
                n1 = stack.pop()
                ans = operators[s](n1, n2)
                stack.append(ans)

        return stack[-1]
