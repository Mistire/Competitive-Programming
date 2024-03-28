class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            prime = nums[i]
            for j in range(i,n):
                prime = gcd(nums[j], prime)
                if prime == k:
                    count += 1
        return count
                