class Node:
    def __init__(self, val: object, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        # Use a front sentinel to make inserting at the front a little easier
        self.head = Node(None)
        self.size = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        pos = 0

        while pos != index:
            curr = curr.next
            pos += 1

        if curr:
            return curr.val

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        pos = 0

        if index == 0:
            self.addAtHead(val)
        else:
            while curr:
                if pos == index - 1:
                    temp = curr.next
                    curr.next = Node(val)
                    curr.next.next = temp
                    self.size += 1
                    break
                curr = curr.next
                pos += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        pos = 0
        prev = curr

        if index < self.size:
            while pos != index:
                prev = curr
                curr = curr.next
                pos += 1

            if index == 0:
                self.head.next = curr.next
            else:
                temp = curr.next
                prev.next = temp
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)