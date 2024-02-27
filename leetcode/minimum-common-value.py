class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # for i in nums1:
        #     if i in nums2:
        #         for i in

        intSet = set(nums1) & set(nums2)
        if len(intSet):
            return min(intSet)
        else:
            return -1
        