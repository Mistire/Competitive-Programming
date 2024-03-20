class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) > 1:
                rh = arr[len(arr)//2:]
                lh = arr[:len(arr)//2]

                merge(lh)
                merge(rh)

                l = 0
                r = 0
                k = 0

                while l < len(lh) and r < len(rh):
                    if lh[l] < rh[r]:
                        arr[k] = lh[l]
                        l += 1
                    else:
                        arr[k] = rh[r]
                        r += 1
                    k += 1
                while l < len(lh):
                    arr[k] = lh[l]
                    k += 1
                    l += 1
                while r < len(rh):
                    arr[k] = rh[r]
                    k += 1
                    r += 1
        merge(nums)
        return nums

