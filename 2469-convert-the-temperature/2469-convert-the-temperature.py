class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = round(celsius + 273.15, 5)
        f = round(celsius * 1.80 + 32.00, 5)
        return [k, f]
        