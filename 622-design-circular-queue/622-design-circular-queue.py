class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        else:
            self.q[(self.head + self.count) % self.k] = value
            self.count += 1
            return True

        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.k
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.q[self.head]
        
    def Rear(self) -> int:
        if self.count == 0:
            return -1
        else:
            return self.q[(self.head + self.count - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()