class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for i, op in enumerate(operations):
            if op[0] == "-" and op[1:].isnumeric():
                record.append(-int(op[1:]))
            elif op.isnumeric():
                record.append(int(op))
            elif op == "+":
                record.append(int(record[-1]) + int(record[-2]))
            elif op == "D":
                record.append(2 * int(record[-1]))
            elif op == "C":
                record.pop()
                
        return sum(record)
