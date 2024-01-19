class Solution:
    def atMostK(self,nums,k):
        i=j=ans=0
        
        while j < len(nums):
            if nums[j] % 2 == 1:
                if k > 0:
                    k -= 1
                else:
                    while nums[i]%2 != 1:
                        i+=1
                    i+=1
            ans+= (j-i+1)
            j+=1
        return ans
            
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums,k)-self.atMostK(nums,k-1)