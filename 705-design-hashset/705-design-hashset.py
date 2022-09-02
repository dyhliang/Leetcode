class MyHashSet:

    def __init__(self):
        self.dict = {}

    def add(self, key: int) -> None:
        self.dict[key] = ""

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.dict.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.dict.keys()


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)