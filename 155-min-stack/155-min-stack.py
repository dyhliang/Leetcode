class Node:
    def __init__(self, value: object, next = None):
        self.value = value
        self.next = next
        

class MinStack:
    def __init__(self):
        self._head = None
        
    def push(self, val: int) -> None:
        if self._head is None:
            self._head = Node(val)
        else:
            top = Node(val)
            top.next = self._head
            self._head = top

    def pop(self) -> None:
        
        if self._head is not None:
            temp = self._head
            self._head = self._head.next
            return temp.value


    def top(self) -> int:
        if self._head is not None:
            return self._head.value
        

    def getMin(self) -> int:
        min_val = self.top()
        
        curr = self._head
        while curr:
            if curr.value < min_val:
                min_val = curr.value
            curr = curr.next
            
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()