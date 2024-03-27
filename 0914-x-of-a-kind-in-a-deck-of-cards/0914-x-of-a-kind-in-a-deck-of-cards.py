class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        part = Counter(deck)
        gcdArr = [i for i in part.values()]
        d = gcd(*gcdArr)
        
        if d == 1:
            return False
        else:
            return True