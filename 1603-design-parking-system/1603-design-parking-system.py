class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.tracking = {
            # [spaces available, spaces parked]
            1: [big, 0],
            2: [medium, 0],
            3: [small, 0]
        }

    def addCar(self, carType: int) -> bool:
        self.tracking[carType][1] += 1
        return self.tracking[carType][1] <= self.tracking[carType][0]


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)