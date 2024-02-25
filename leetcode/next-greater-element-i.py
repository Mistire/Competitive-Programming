class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        numIdx = {num:i for i,num in enumerate(nums1)}

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                idx = numIdx[val]
                res[idx] = cur
            if cur in numIdx:
                stack.append(cur)
        return res
        

                    

            