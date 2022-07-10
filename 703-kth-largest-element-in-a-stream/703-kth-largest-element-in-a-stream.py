class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.kth = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[self.kth * -1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)