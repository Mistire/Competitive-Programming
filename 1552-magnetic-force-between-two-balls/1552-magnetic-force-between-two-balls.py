class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 0
        right = position[-1]
        

        def is_valid(gap):
            count = 0
            max_gap = float('-inf')
            for basket in position:
                if basket - max_gap >= gap:
                    max_gap = basket
                    count += 1
            return count >= m
            

        

        while left < right:
            mid = (left+right) // 2
            if is_valid(mid+1):
                left = mid + 1
            else:
                right = mid
        
        return left

       
        
        



         



    

