class MyQueue:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # use temp to store the queue backwards, turn it backwards again after popping
        temp = self.queue[::-1]
        res = temp.pop()
        self.queue = temp[::-1]
        return res

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()