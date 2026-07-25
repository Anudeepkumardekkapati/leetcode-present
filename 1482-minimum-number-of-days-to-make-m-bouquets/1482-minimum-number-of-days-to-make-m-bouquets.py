class Solution:
    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        
        if m*k> len(bloomday):
            return -1
            
        def fun(day,bloomday,m,k):

            bak=0
            count=0
            
            for i in bloomday:
                if i<=day:
                    count+=1
                    if count==k:
                        bak+=1
                        count=0
                else:
                    count=0
            return bak>=m


        
        l=min(bloomday)

        r=max(bloomday)
        ans=-1
        while(l<=r):
            mid=(l+r)//2

            if fun(mid,bloomday,m,k):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

            