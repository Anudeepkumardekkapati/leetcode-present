class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        
        def fun(maxarr,nums,k):
            subs=1
            sums=0
            
            for i in nums:

                if sums+i<=maxarr:
                    sums+=i
                
                else:
                    subs+=1
                
                    
                    sums=i
            return subs<=k

        
        l=max(nums)
        r=sum(nums)+1
        ans=-1
        while(l<=r):
            mid=(l+r)//2
            if fun(mid,nums,k):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans 

                
        
            

        