from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.t = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.t[start] = 1 + self.t.get(start, 0)
        self.t[end] = self.t.get(end, 0) - 1
        cur = 0
        res = 0
        
        for times in self.t.values():
            cur += times
            res = max(cur, res)
        
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)