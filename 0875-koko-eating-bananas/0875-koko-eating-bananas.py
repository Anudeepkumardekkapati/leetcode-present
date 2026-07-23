class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        
        def fun(k,h,nums):

            for i in nums:
                val=(i+k-1)//k
                h-=val
            return h>=0
        
        l=1
        r=max(nums)

        while(l<r):
            mid=(l+r)//2
            if fun(mid,h,nums):
                r=mid
            else:
                l=mid+1
        return l







        