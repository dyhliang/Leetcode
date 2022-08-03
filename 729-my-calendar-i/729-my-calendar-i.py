class MyCalendar:

    def __init__(self):
        self.cal = []


    def book(self, start: int, end: int) -> bool:
        for bookings in self.cal:
            if bookings[0] < end and start < bookings[1]:
                return False

        self.cal.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)