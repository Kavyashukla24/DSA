class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       n=len(nums)
       d={0:1}
       c=0
       for i in range(1,n):
        nums[i]=nums[i]+nums[i-1]
       for i in range(n):
        nums[i]=nums[i]%k
       for i in range(n):
        extra=nums[i]-0
        if extra in d:
            c+=d[extra]
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
       return c