class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        right = len(nums)
        checked = set()

        for i in range(right):
            if i not in checked:
                cycleSet = set()
                while True:
                    if i in cycleSet:
                        return True
                    checked.add(i)
                    cycleSet.add(i)

                    left, i = i, (i+nums[i]) % right

                    #unicycle
                    if left == i:
                        break
                    #sign diff
                    if nums[left] > 0 != nums[i] < 0:
                        break

        return False


        