class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # curSum = 0
        # prefixSums = {0:1}
        
        # for n in nums:
        #     curSum += n
        #     diff = curSum - k
        #     res += prefixSums.get(diff, 0)
        #     prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        # return res

        sumDict = {0:1}
        preSum = 0
        count = 0

        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - k in sumDict:
                count += sumDict[preSum - k]

            if preSum in sumDict:
                sumDict[preSum] += 1
            else:
                sumDict[preSum] = 1

        return count






















        