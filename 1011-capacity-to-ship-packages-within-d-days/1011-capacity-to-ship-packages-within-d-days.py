class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        def fun(k,nums,days):
            
            sums=0
            used=1
            for i in nums:
                if sums+i>k:
                    sums=i
                    used+=1
                else:
                    sums+=i
            return used<=days
        l=max(nums)
        r=sum(nums)+1
        ans=-1
        while(l<=r):

            mid=(l+r)//2

            if fun(mid,nums,days):

                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        
        