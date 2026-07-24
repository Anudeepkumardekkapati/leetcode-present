class Solution:
    def minSpeedOnTime(self, nums: List[int], hour: float) -> int:
       

    

        def fun(k,nums,hour):
            some=0

            for i in range(len(nums)-1):
                val=nums[i]
                some+= (val+k-1)//k
            some+=nums[-1]/k
            
            return some<=hour

        l=1
        r=10**7+1
        ans=-1
        while(l<=r):
            mid=(l+r)//2
            if fun(mid,nums,hour):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans


                