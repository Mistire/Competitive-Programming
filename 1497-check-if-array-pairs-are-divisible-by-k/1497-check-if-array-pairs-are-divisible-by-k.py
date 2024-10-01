class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        left = 0
        right = len(arr) - 1

        while left <= right:
            if (arr[left] + arr[right]) % k != 0:
                return False
            left += 1
            right -= 1
        return True