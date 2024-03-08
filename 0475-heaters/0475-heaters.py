class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0

        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = left + (right - left) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            if left == 0:
                min_radius = max(min_radius, abs(heaters[left] - house))
            elif left == len(heaters):
                min_radius = max(min_radius, abs(heaters[left - 1] - house))
            else:
                min_radius = max(min_radius, min(abs(heaters[left] - house), abs(heaters[left - 1] - house)))

        return min_radius



