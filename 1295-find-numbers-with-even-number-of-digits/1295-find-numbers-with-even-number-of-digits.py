class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0

        for i in nums:
           
            s=(str(i))
            count=0
            for j in s:
                # print(j)
                count+=1
            if(count%2==0):
                ans+=1
        return ans
            
        