class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        left, right = 0, 10**9
        
        heaters.sort()
        houses.sort()
        # return 1

        while left <= right:
            rad = (left+right) // 2
            hoP, heaP = 0, 0
            while heaP < len(heaters) and hoP < len(houses):
                if abs(heaters[heaP] - houses[hoP]) <= rad:
                    hoP += 1
                else:
                    heaP += 1
            
            if hoP == len(houses):
                right = rad - 1
            elif heaP == len(heaters):
                left = rad + 1

        return left



