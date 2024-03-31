class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1) if n % i == 0]
        return nums[k-1] if len(nums) >= k else -1

        