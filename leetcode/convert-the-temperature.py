class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kel = float(celsius + 273.15)
        fah = float(9/5 * celsius + 32)
        return [kel, fah]