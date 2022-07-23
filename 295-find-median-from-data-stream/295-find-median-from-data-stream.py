class MedianFinder:

    def __init__(self):
        self._data = []

    def addNum(self, num: int) -> None:
        self._data.append(num)

    def findMedian(self) -> float:
        self._data.sort()
        data_len = len(self._data)
        if data_len % 2 == 0:
            return (self._data[data_len // 2] + self._data[data_len // 2 - 1]) / 2
        else:
            return self._data[len(self._data) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()