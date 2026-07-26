class Solution:
    def maxDistance(self, nums: List[int], m: int) -> int:
      
        nums.sort()
       
        def fun(dist,nums,m):



            count=1
            last=nums[0]
            for i in range(1,len(nums)):
                # print(nums[i])
                if nums[i]-last >=dist:
                   
                    count+=1
                    last=nums[i]
               
                if count>=m:
                    break

            return count>=m

        

        l=1
        r=max(nums)+1
        ans=-1
        while(l<=r):
            mid=(l+r)//2

            if fun(mid,nums,m):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        

                
            
        