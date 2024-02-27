class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        res= []
        found = False

        while not found:
            if numbers[l] + numbers[r] == target:
                res.append((l + 1))
                res.append((r + 1))
                found = True
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return res
            